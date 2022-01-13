from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from game.models import Category, CategoryData, Team
from game.serializers import CategorySerializer, CategoryDataSerializer, TeamSerializer
from rest_framework import views

class CategoryList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TeamList(views.APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = [TeamSerializer]

    def post(self, request):
        serializer = TeamSerializer(data=request.data)
        print(serializer)
        data = Team.objects.filter(user=1)
        return data


class CategoryDataList(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = [CategoryDataSerializer]
    queryset = CategoryData.objects.all()

    def get_queryset(self):
        category = self.kwargs.get('category_id')
        return CategoryData.objects.filter(category=category)
