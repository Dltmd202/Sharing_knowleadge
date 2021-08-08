from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.socialaccount.models import SocialToken

# 소셜 로그인 어댑터
class GoogleAccountAdapter(DefaultSocialAccountAdapter):
    def save_user(self, request, sociallogin, form):
        user = super(GoogleAccountAdapter, self).save_user(request, sociallogin, form)
        extra_data = sociallogin.account.extra_data
        provider = sociallogin.account.provider
        if provider == 'google':
            if 'picture' in extra_data:
                user.user_pic_url = extra_data['picture']
        elif provider == 'kakao':
            if 'properties' in extra_data:
                if 'profile_image' in extra_data['properties']:
                    user.user_pic_url = extra_data['properties']['profile_image']
        elif provider == 'naver':
            if 'profile_image' in extra_data:
                user.user_pic_url = extra_data['profile_image']
        user.save()
        return user