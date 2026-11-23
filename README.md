# Задача 28: Мессенджер учебных групп

**Студент:** Яцко В.А.

## Постановка

Групповой чат для курса. User: вступить в группу, писать, читать историю. Tech: модель сообщения, пагинация. OpenAPI: группы, сообщения (post/list), участники, поиск по тексту (хотя бы описанный эндпоинт).

## Обзор проекта

Мессенджер учебных групп: студенты курса вступают в группу, пишут сообщения, читают историю постранично и ищут по тексту.
Реализация API в этой работе не требуется: документация и спецификация описывают контракт (допустима заглушка/mock).

## Документация

- [Руководство пользователя](docs/user.md): доступ, сценарии (вступить, писать, читать историю, искать, выйти), FAQ и типичные ошибки
- [Техническая документация](docs/tech.md): архитектура, модель сообщения, пагинация, поиск, договорённости, конфигурация
- OpenAPI: [`openapi.yaml`](openapi.yaml) (OpenAPI 3.0.3, 10 операций, 7 схем)

## Операции API

| Метод и путь | Назначение |
|---|---|
| `GET /groups` | список групп (публичный) |
| `POST /groups` | создать группу |
| `GET /groups/{groupId}` | информация о группе |
| `GET /groups/{groupId}/members` | **участники** группы |
| `POST /groups/{groupId}/members` | вступить в группу |
| `DELETE /groups/{groupId}/members/me` | выйти из группы |
| `GET /groups/{groupId}/messages` | **история** сообщений с пагинацией (`limit`, `before_id`) |
| `POST /groups/{groupId}/messages` | **отправить** сообщение |
| `GET /groups/{groupId}/messages/search` | **поиск по тексту** (`q`) |
| `GET /users/me/groups` | мои группы |

## Как открыть и проверить спецификацию

```bash
pip install openapi-spec-validator pyyaml
python scripts/validate_spec.py          # проверка структуры OpenAPI 3.x; ожидаемо: "OK: OpenAPI 3.0.3, операций: 10 ..."

python -m http.server 8080               # из корня репозитория
# открыть http://localhost:8080/docs/swagger.html: интерактивный Swagger UI
```

Без установки: вставить содержимое `openapi.yaml` в https://editor.swagger.io.
Mock-сервер по спецификации: `npx @stoplight/prism-cli mock openapi.yaml` (см. `docs/tech.md`).

## Структура

```
README.md
openapi.yaml
docs/user.md
docs/tech.md
docs/swagger.html
scripts/validate_spec.py
```
