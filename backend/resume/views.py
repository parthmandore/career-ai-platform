from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Resume
from .serializers import ResumeSerializer

class ResumeUploadView(generics.CreateAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)