from api.dto.aluno import aluno_create_dto, aluno_update_dto, aluno_delete_dto
from django.views.decorators.http import require_http_methods
from core.decorator import has_data_body, validate_dataclass
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpRequest
from alunos.models import Alunos, Responsavel
from oficinas.models import Oficinas
from core.models import User
import json


@csrf_exempt
@require_http_methods(["POST"])
@validate_dataclass(aluno_create_dto.CreateAluno)
@has_data_body
def create_aluno(request: HttpRequest) -> JsonResponse:
    data = json.loads(request.body) 

    try:
        responsavel = Responsavel.objects.get(id=data['responsavel'])

    except Responsavel.DoesNotExist:
        return JsonResponse(
            {
                'success': False,
                'msg': 'Responsavel does not exists'
            }, 
            status=422
        )

    try:
        user = User(
            username = data['username'],
            nome = data['nome'],
            cpf = data['cpf'],
            password = make_password(data['senha']),
            data_nasc = data['data_nasc'],
            endereco = data['endereco'],
            bairro = data['bairro'],
            cidade = data['cidade'],
            numero = data['numero'],
            uf = data['uf'],
            cep = data['cep']
        )
        user.save()

    except Exception:
        return JsonResponse(
            {
                'success': False,
                'msg': 'Username or CPF duplicate'
            }, 
            status=422
        )

    aluno = Alunos(
        responsavel = responsavel,
        user = user
    )
    aluno.save()

    return JsonResponse(
        {
            'success': True,
            'id': aluno.id,
        }, 
        status=201
    )


@csrf_exempt
@require_http_methods(["POST"])
@validate_dataclass(aluno_create_dto.CreateResponsavel)
@has_data_body
def create_responsavel(request: HttpRequest) -> JsonResponse:
    data = json.loads(request.body) 

    try:
        responsavel = Responsavel(
            nome = data['nome'],
            cpf = data['cpf'],
            data_nasc = data['data_nasc'],
            tel = data['tel']
        )
        responsavel.save()

    except Exception:
        return JsonResponse(
            {
                'success': False,
                'msg': 'CPF duplicate'
            }, 
            status=422
        )

    return JsonResponse(
        {
            'success': True,
            'id': responsavel.id,
        }, 
        status=201
    )


@csrf_exempt
@require_http_methods(["GET"])
def get_aluno_by_id(request: HttpRequest, id: str) -> JsonResponse:
    aluno = Alunos.objects.filter(id=id, deleted=0).values(
        "responsavel",
        "created_at",
        "deleted",
        "user__id",
        "user__nome",
        "user__cpf",
        "user__cep",
        "user__cidade",
        "user__endereco",
        "user__bairro",
        "user__numero",
        "user__uf",
        "user__cep",
        "user__data_nasc",
    )

    if not aluno.exists():
        return JsonResponse(
            {
                'success': False,
                'msg': 'Id not found'
            }, 
            status=422
        )

    return JsonResponse(
        {
            'success': True,
            'aluno': aluno[0]
        }, 
        status=200
    )


@csrf_exempt
@require_http_methods(["GET"])
def get_responsavel_by_id(request: HttpRequest, id: str) -> JsonResponse:
    responsavel = Responsavel.objects.filter(id=id, deleted=0).values()

    if not responsavel.exists():
        return JsonResponse(
            {
                'success': False,
                'msg': 'Id not found'
            }, 
            status=422
        )

    return JsonResponse(
        {
            'success': True,
            'responsavel': responsavel[0]
        }, 
        status=200
    )


@csrf_exempt
@require_http_methods(["GET"])
def get_aluno(request: HttpRequest) -> JsonResponse:
    aluno = Alunos.objects.filter(deleted=0).order_by("-id").values(
        "responsavel",
        "created_at",
        "deleted",
        "user__id",
        "user__nome",
        "user__cpf",
        "user__cep",
        "user__cidade",
        "user__endereco",
        "user__bairro",
        "user__numero",
        "user__uf",
        "user__cep",
        "user__data_nasc",
    )[:30]

    return JsonResponse(
        {
            'success': True,
            'alunos': list(aluno),
        }, 
        status=200
    )


@csrf_exempt
@require_http_methods(["PUT"])
@validate_dataclass(aluno_update_dto.UpdateAluno)
@has_data_body
def update_aluno(request: HttpRequest) -> JsonResponse:
    data = json.loads(request.body) 

    try:
        aluno = Alunos.objects.get(id=data['id'], deleted=0)

    except Alunos.DoesNotExist:
        return JsonResponse(
            {
                'success': False,
                'msg': 'Aluno does not exists'
            }, 
            status=422
        )

    try:
        User.objects.filter(id=aluno.user_id).update(
            data_nasc = data['data_nasc'],
            endereco = data['endereco'],
            bairro = data['bairro'],
            cidade = data['cidade'],
            numero = data['numero'],
            uf = data['uf'],
            cep = data['cep']
        )

    except Exception:
        return JsonResponse(
            {
                'success': False,
                'msg': 'Error'
            }, 
            status=422
        )

    return JsonResponse(
        {
            'success': True,
            'msg': 'Updated data'
        }, 
        status=200
    )


@csrf_exempt
@require_http_methods(["DELETE"])
@validate_dataclass(aluno_delete_dto.DeleteAluno)
@has_data_body
def delete_aluno(request: HttpRequest) -> JsonResponse:
    data = json.loads(request.body) 

    aluno = Alunos.objects.filter(id=data['id'], deleted=0)

    if not aluno.exists():
        return JsonResponse(
        {
            'success': False,
            'msg': 'Aluno does not exists'
        }, 
        status=422
    )
    
    aluno.update(deleted=1)

    return JsonResponse(
        {
            'success': True,
        }, 
        status=200
    )