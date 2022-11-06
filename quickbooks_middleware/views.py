from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from .serializers import *
from rest_framework.response import Response
from django.core.files.storage import default_storage
import base64


class Order(ViewSet):
    http_method_names = ['post']

    @action(detail=False, methods=['post'], name='ObtainFile', url_path='retrieve/')
    def obtain_files(self, request):
        try:
            delivery_id = request.data['delivery_id']
            delivery = Deliveries.objects.get(id_delivery=delivery_id)
            documents_serialized = []
            for document in delivery.documentsdelivery_set.all():
                doc_dict = dict(DocumentsDeliverySerializer(document).data)
                doc_dict["kind"] = dict(DocumentKindSerializer(document.document_kind).data)
                documents_serialized.append(doc_dict)
            documents = []
            try:
                for document in documents_serialized:
                    if default_storage.exists(document["document_name"]):
                        documents.append(
                            {"file": base64.b64encode(default_storage.open(document["document_name"]).read()),
                             "type": document["document_type"], "kind": document["kind"]})
                delivery = dict(DeliveriesSerializer(delivery).data)
                delivery["documents"] = documents
                return Response(data=delivery, status=status.HTTP_200_OK)
            except:
                pass
            return Response(data={"error": "No se pudo obtener el detalle de la orden"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except ObjectDoesNotExist:
            return Response({"error": "Orden no disponible"}, status=status.HTTP_404_NOT_FOUND)
        except KeyError:
            return Response({"error": "Petición inválida"}, status=status.HTTP_400_BAD_REQUEST)

