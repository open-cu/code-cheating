### набросок пока что без запуска API и без работы с выхлопом dolos'а

Допустим, мы уже склеили файлики каждого студента и получили структуру вида:
![Image](https://github.com/user-attachments/assets/a57dc881-abe8-4c9e-ba61-9d13df215e5d)

(здесь у каждого студента свой склеенный файлик)

Предварительно устанавливаем dolos CLI через docker: `docker pull ghcr.io/dodona-edu/dolos-cli:latest`

### запускать под linux
`cd sample`

`python3 dolos.py`


после работы скрипта dolos сгенерит структуру вида:
![Image](https://github.com/user-attachments/assets/387119ce-e4c2-4d4b-9018-d3a6cfc34351)

это грубо говоря бд с четырьмя табличками
в pairs - нужные нам similarity по каждой паре студентов