
from django.views.generic import  DetailView, UpdateView
from .models import Answer, Comment
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets, serializers
from comment.forms import  CommentForm

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

# 코멘트 만들기
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    # queryset 정의
    def get_queryset(self):
        queryset = self.queryset
        search_pk = self.request.query_params.get('pk', None)
        search_keyword = self.request.query_params.get('keyword', None)
        query_list = []
        if search_pk:
            queryset = queryset.filter(pk=search_pk)
        if search_keyword:
            queryset = queryset.filter(
                Q(comment_desc__contains=search_keyword)
                | Q(category_id__slug__contains=search_keyword)
            ).distinct()
        return queryset

    @action(detail=False, methods=['post'])
    def create_comment(self, request):
        comment = CommentSerializer(data=request.data)
        if comment.is_valid():
            comment.save()
            return Response(comment.data, status=status.HTTP_201_CREATED)
        return Response(comment.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetail(DetailView):
    model = Comment

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CommentDetail, self).get_context_data()
        context['no_category_answer_count'] = Comment.objects.filter(user_id=None).count()
        context['comment_form'] = CommentForm
        return context

def new_comment(request, pk):
    if request.user.is_authenticated:
        answer = get_object_or_404(Answer, pk=pk)
        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.anwer_id = answer
                comment.comment_desc = comment
                comment.user_id = request.user
                comment.save()
                return comment
        else:
            return redirect(Comment.get_absolute_url())
    else:
        raise PermissionDenied

class CommentEdit(LoginRequiredMixin, UpdateView):
    model = Comment
    fields = ['comment_date', 'comment_desc']

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().user_id:
            return super(CommentEdit, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied
