from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Resume
from .serializers import ResumeSerializer
from .ai_service import analyze_resume

from ai.ai_service import analyze_resume
from rest_framework.response import Response

class ResumeUploadView(generics.CreateAPIView):

    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):

        resume = serializer.save(user=self.request.user)

        result = analyze_resume(resume.pdf.path)

        self.analysis = result

    def create(self, request, *args, **kwargs):

        response = super().create(request, *args, **kwargs)

        return Response({

            "message": "Resume uploaded successfully",

            "analysis": self.analysis

        })