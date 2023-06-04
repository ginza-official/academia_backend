from rest_framework import serializers
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
import os
from .models import *

# Create your views here.


# kurslar
class CourseSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField()
    teacher_fistname = serializers.CharField(source='teacher.fistname')
    teacher_lastname = serializers.CharField(source='teacher.lastname')
    teacher_image = serializers.ImageField(source='teacher.image')
    videos_count = serializers.SerializerMethodField()

    def get_videos_count(self, course):
        return course.video_set.count()
    class Meta:
        model = Course
        fields = (
            'id',
            'title',
            'icon',
            'description',
            'price',
            'price_per',
            'created_at',
            'updated_at',
            'token_uuid',
            'teacher',
            'teacher_fistname',
            'teacher_lastname',
            'teacher_image',
            'videos_count',

        )





class CoursesListAPIView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_queryset(self):
        return Course.objects.all()


class CoursesDetailAPIView(RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer



class CoursesCreateAPIView(CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CoursesUpdateAPIView(UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CoursesDeleteAPIView(DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


# teachers
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class TeachersListAPIView(ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def get_queryset(self):
        return Teacher.objects.all()


class TeachersDetailAPIView(RetrieveAPIView):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()


class TeachersCreateAPIView(CreateAPIView):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()


class TeachersUpdateAPIView(UpdateAPIView):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()


class TeachersDeleteAPIView(DestroyAPIView):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()


# contact_us

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class ContactCreateAPIView(CreateAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


# blogposts

class BlogpostSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='author.username')
    created_at = serializers.DateTimeField(format='%Y-%m-%d', read_only=True)
    comments_count = serializers.SerializerMethodField()

    def get_comments_count(self, blogpost):
        return blogpost.postcomments_set.count()
    class Meta:
        model = Blogpost
        fields =('id','title','image','description','created_at','username','comments_count')


class BlogpostsListAPIView(ListAPIView):
    serializer_class = BlogpostSerializer
    queryset = Blogpost.objects.all()

    def get_queryset(self):
        return Blogpost.objects.all()


class BlogpostsDetailAPIView(RetrieveAPIView):
    serializer_class = BlogpostSerializer
    queryset = Blogpost.objects.all()


class BlogpostsCreateAPIView(CreateAPIView):
    serializer_class = BlogpostSerializer
    queryset = Blogpost.objects.all()


class BlogpostsUpdateAPIView(UpdateAPIView):
    serializer_class = BlogpostSerializer
    queryset = Blogpost.objects.all()


class BlogpostsDeleteAPIView(DestroyAPIView):
    serializer_class = BlogpostSerializer
    queryset = Blogpost.objects.all()


# post_comments

class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComments
        fields = '__all__'


class BlogPostSerializer(serializers.ModelSerializer):
    comments = PostCommentSerializer(many=True, read_only=True)
    username = serializers.CharField(source='user.username')
    fist_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    image = serializers.ImageField(source='user.avatar')

    class Meta:
        model = PostComments
        fields = (
            'id',
            'post',
            'user',
            'username',
            'fist_name',
            'last_name',
            'image',
            'comment',
            'created_at',
            'updated_at',
            'comments',
            'updated_at',
        )


class BlogpostsDetailCommentsAPIView(ListAPIView):
    serializer_class = BlogPostSerializer

    def get_queryset(self):
        post_id = self.kwargs['pk']
        return PostComments.objects.filter(post_id=post_id)


class PostCommentsListAPIView(ListAPIView):
    serializer_class = PostCommentSerializer
    queryset = PostComments.objects.all()

    def get_queryset(self):
        return PostComments.objects.all()


class PostCommentsDetailAPIView(RetrieveAPIView):
    serializer_class = PostCommentSerializer
    queryset = PostComments.objects.all()


class PostCommentsCreateAPIView(CreateAPIView):
    serializer_class = PostCommentSerializer
    queryset = PostComments.objects.all()


class PostCommentsUpdateAPIView(UpdateAPIView):
    serializer_class = PostCommentSerializer
    queryset = PostComments.objects.all()


class PostCommentsDeleteAPIView(DestroyAPIView):
    serializer_class = PostCommentSerializer
    queryset = PostComments.objects.all()


# news

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class NewsListAPIView(ListAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()

    def get_queryset(self):
        return News.objects.all()


class NewsCreateAPIView(CreateAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()


# test

class VideoSerializer(serializers.ModelSerializer):
    file_path = serializers.SerializerMethodField()

    def get_file_path(self, obj):
        return obj.file.url

    class Meta:
        model = Video
        fields = ['title', 'file', 'file_path']

class CoursesDetailVideoAPIView(ListAPIView):
    serializer_class = VideoSerializer
    def get_queryset(self, *args, **kwargs):
        course_id = self.kwargs['pk']
        return Video.objects.filter(course_id=course_id)






