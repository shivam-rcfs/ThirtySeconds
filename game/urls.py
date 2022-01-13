from django.urls import path
from game.views import CategoryList, CategoryDataList, TeamList

urlpatterns = [
    path('category/', CategoryList.as_view(), name="category"),
    path('team/', TeamList.as_view(), name="team"),
    path('words/', CategoryDataList.as_view(), name="words")
]
