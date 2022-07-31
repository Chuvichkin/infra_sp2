<!DOCTYPE html>
<html lang="en" data-color-mode="auto" data-light-theme="light" data-dark-theme="dark" data-a11y-animated-images="system">
  <head>
    <meta charset="utf-8">
<h3 dir="auto" align="center">Спринт 15. Проект: запуск docker-compose.</h3>
<h3 dir="auto"><a id="user-content-описание" class="anchor" aria-hidden="true" href="#описание"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Описание.</h3>
<p dir="auto">Данный проект был создан в целях тренировки контейнеризации проектов. В данном случае в контейнер упаковывается проект api_yamdb (<a href="https://github.com/Chuvichkin/api_yamdb">https://github.com/Chuvichkin/api_yamdb</a>).</p>
<p dir="auto">Проект YaMDb собирает отзывы пользователей на произведения. Произведения разделяются на категории. Список категорий может быть расширен администратором. Произведению может быть присвоен жанр. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы (Review) и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.</p>

<h4 dir="auto"><a id="user-content-инструкция-по-развёртыванию" class="anchor" aria-hidden="true" href="#инструкция-по-развёртыванию"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Инструкция по установке проекта.</h4>
<ul dir="auto">
<li>Произвести клонирование репозитория и перейти в его директорию:</li>
</ul>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" data-snippet-clipboard-copy-content="git clone https://github.com/Chuvichkin/infra_sp2"><pre><span class="pl-s1">git</span> <span class="pl-s1">clone</span> <span class="pl-s1">https</span>:<span class="pl-s1">//</span><span class="pl-s1">github</span>.<span class="pl-s1">com</span><span class="pl-s1">/</span><span class="pl-s1">Chuvichkin</span><span class="pl-s1">/</span><span class="pl-s1">infra_sp2</span>.<span class="pl-s1">git</span></pre></div>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" data-snippet-clipboard-copy-content="cd infra_sp2"><pre><span class="pl-s1">cd</span> <span class="pl-s1">infra_sp2</span></pre></div>

<ul dir="auto">
<li>В директории infra создайте файл .env с переменными окружения для работы с базой данных:</li>
</ul>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto" data-snippet-clipboard-copy-content="DJANGO_KEY='your Django secret key'
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД"><pre class="notranslate"><code>DJANGO_KEY='your Django secret key'
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД
</code></pre></div>

<ul dir="auto">
<li>Из директории infra выполните команду для разворачивания контейнеров:</li>
</ul>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" data-snippet-clipboard-copy-content="sudo docker-compose up -d"><pre><span class="pl-s1">sudo docker-compose up -d</span></pre></div>

<ul dir="auto">
<li>Теперь в контейнере web нужно выполнить миграции:</li>
</ul>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" data-snippet-clipboard-copy-content="sudo docker-compose up -d"><pre><span class="pl-s1">sudo docker-compose exec web python manage.py migrate</span></pre></div>

<ul dir="auto">
<li>Создать суперпользователя:</li>
</ul>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" data-snippet-clipboard-copy-content="sudo docker-compose up -d"><pre><span class="pl-s1">sudo docker-compose exec web python manage.py createsuperuser</span></pre></div>

<ul dir="auto">
<li>Собрать статику:</li>
</ul>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" data-snippet-clipboard-copy-content="sudo docker-compose up -d"><pre><span class="pl-s1">sudo docker-compose exec web python manage.py collectstatic --no-input</span></pre></div>

<ul dir="auto">
<li>Cоздать дамп(резервную копию) базы можно командой:</li>
</ul>
<div class="highlight highlight-source-python notranslate position-relative overflow-auto" data-snippet-clipboard-copy-content="sudo docker-compose up -d"><pre><span class="pl-s1">sudo docker-compose exec web python manage.py dumpdata > fixtures.json</span></pre></div>


<h4 dir="auto"><a id="user-content-язык" class="anchor" aria-hidden="true" href="#язык"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Язык</h4>
<ul dir="auto">
<li>Python</li>
</ul>
<h4 dir="auto"><a id="user-content-стек-технологий" class="anchor" aria-hidden="true" href="#стек-технологий"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>В проекте использованы технологии</h4>
<ul dir="auto">
<li>Python</li>
<li>Django</li>
<li>Django REST Framework</li>
<li>Git</li>
<li>Docker</li>
</ul>
<h3 dir="auto"><a id="user-content-создатель-проекта" class="anchor" aria-hidden="true" href="#создатель-проекта"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Автор проекта</h3>
<ul dir="auto">
<li>Чувычкин Сергей</li>
</ul>
</article>
  </div>