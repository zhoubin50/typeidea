from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.contrib.admin.models import LogEntry

from blog.models import Category, Tag, Post
from blog.adminforms import PostAdminForm
from typeidea.custom_site import custom_site
from typeidea.base_admin import BaseOwnerAdmin


# Register your models here.
class PostInline(admin.TabularInline):
    fields = ('title', 'desc')
    extra = 1
    model = Post


@admin.register(Category, site=custom_site)
class CategoryAdmin(BaseOwnerAdmin):
    inlines = [PostInline, ]
    # 后台管理界面展示的字段
    list_display = ('name', 'status', 'is_nav', 'created_time', 'post_count')

    # 新建时填写的字段
    fields = ('name', 'status', 'is_nav')

    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = '文章数目'


class CategoryOwnerFilter(admin.SimpleListFilter):
    """
    自定义过滤器，只展示当前用户分类
    """
    title = '分类过滤器'
    parameter_name = 'owner_category'

    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list('id', 'name')

    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=self.value())
        return queryset


@admin.register(Tag, site=custom_site)
class TagAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'created_time')
    fields = ('name', 'status')


@admin.register(Post, site=custom_site)
class PostAdmin(BaseOwnerAdmin):
    form = PostAdminForm
    # 列表页展示字段
    list_display = ['title', 'category', 'status', 'created_time', 'owner', 'operator', ]
    # 哪些字段可以作为链接，点击他们可以进入编辑页
    list_display_links = []

    # 配置过滤器，设置过滤器字段
    # list_filter = ['category__name']
    list_filter = [CategoryOwnerFilter]
    # 配置搜索字段
    search_fields = ['title', 'category__name']

    exclude = ('owner',)

    # fields = (('category', 'title'), 'desc', 'status', 'content', 'tag',)

    fieldsets = (
        ('基础配置', {
            'description': '基础配置描述',
            'fields': ('title', 'category', 'status')
        }),
        ('内容', {
            'fields': ('desc', 'content')
        }),
        ('额外信息', {
            'classes': ('collapse',),
            'fields': ('tag',)
        })
    )

    # 是否在列表顶部展示动作条
    actions_on_top = True
    # 是否在列表底部展示动作条
    actions_on_bottom = True
    # 在顶部展示保存，编辑按钮
    save_on_top = True

    # 自定义字段
    def operator(self, obj):
        return format_html('<a href="{}">编辑</a>', reverse('cus_admin:blog_post_change', args=(obj.id,)))

    # 自定义字段表头文字
    operator.short_description = '操作'


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('object_repr', 'object_id', 'action_flag', 'user', 'change_message',)
