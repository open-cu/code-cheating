# code-cheating
Обёртка для проверки кода на списывание участников контеста

## Установка и поднятие Dolos API
### Клонирование репозитория, включая исходный код Dolos
`git clone --recursive https://github.com/open-cu/code-cheating.git`
### Поднятие Dolos API
`cd dolos/ && docker-compose pull && docker pull ghcr.io/dodona-edu/dolos-cli:latest && docker-compose up`

По умолчанию API будет доступен на http://localhost:3000/


## Использование Dolos API
### Документация: https://dolos.ugent.be/docs/api.html