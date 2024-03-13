from rest_framework import generics, permissions
from .models import Task, Label
from .serializers import TaskSerializer, LabelSerializer
from .permissions import IsOwnerOrReadOnly

class TaskListCreate(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        # Filter tasks by the current user
        return Task.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TaskRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        # Filter tasks by the current user
        return Task.objects.filter(owner=self.request.user)

class LabelListCreate(generics.ListCreateAPIView):
    serializer_class = LabelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Filter labels by the current user
        return Label.objects.filter(owner=self.request.user)

class LabelRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Filter labels by the current user
        return Label.objects.filter(owner=self.request.user)
