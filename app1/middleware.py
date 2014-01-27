import re

class LastSiteUrl(object):
    def is_admin_url(self, url):
        return re.search('^(http:\/\/.*){0,1}\/admin\/', url) is not None

    def process_request(self, request):
        if self.is_admin_url(request.path) and \
            not self.is_admin_url(request.META.get('HTTP_REFERER','')):
            request.session['last_site_url'] = request.META.get('HTTP_REFERER','')
            
