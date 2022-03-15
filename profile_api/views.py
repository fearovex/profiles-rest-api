from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from profile_api import serializers


class HellAPIView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
      """Return a list of APIView features"""
      an_apiview = [
        'Uses HTTP methods as function (get, post, patch, put, delete)',
        'Is similar to a traditional Django View',
        'Gives you the most control over your logic',
        'Is mapped manually to URLs',
      ]

      return Response({'message': 'Hello!', 'an_apiview': an_apiview})
    
    
    def post(self, request, format=None):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            # message = 'Hello {0}'.format(name)
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
          
    def put(self, request, pk=None):
        """Handle updating an object"""        
        return Response({'method': 'PUT'})
      
      
    def patch(self, request, pk=None):
        """Handle a partial updating an object"""        
        return Response({'method': 'PATCH'})
      
      
    def delete(self, request, pk=None):
        """Delete an object"""        
        return Response({'method': 'DELETE'})
