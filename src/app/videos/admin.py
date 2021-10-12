from django.contrib import admin
from .models import VideoAllProxy, VideoPublishedProxy


class VideoAllProxyAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'state', 'is_published']
    search_fields = ['title']
    list_filter = ["state", "active"]
    readonly_fields = ['id', 'is_published', 'publish_timestamp']
    class Meta:
        model = VideoAllProxy


class VideoPublishedProxyAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    search_fields = ['title']
    readonly_fields = ['id', 'is_published', 'publish_timestamp']

    class Meta:
        model = VideoAllProxy
    
    def get_queryset(self, request):
        return VideoPublishedProxy.objects.filter(active=True)


admin.site.register(VideoAllProxy, VideoAllProxyAdmin)
admin.site.register(VideoPublishedProxy, VideoPublishedProxyAdmin)
