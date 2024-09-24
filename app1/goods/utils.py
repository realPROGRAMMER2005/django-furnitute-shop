from goods.models import Products
from django.db.models import Q
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank


def q_search(query):

      if query.isdigit() and len(query) <= 5:
            return Products.objects.filter(id=int(query))
      
      vector = SearchVector('name', 'description')
      query = SearchQuery(query)

      return Products.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gte=0.0).order_by('-rank')
      

      
      
