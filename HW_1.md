1. Dragonfly - имеет СР в силу того, что основан на базе данных Redis, которая является СР базой данных. А Redis является СР из-за:
   1. С - из-за того, что это однонодовая БД и не требуется синхронизации данных между нодами
   2. P - снова же, из-за своей однонодовости позволяет каждому отдельному инстансу БД обслуживать клиентов 
2. ScyllaDB - также основана на другой известной БД - Cassandra, что говорит о AP
   1. A - из-за цикличной архитектуры, которая позволяет перенаправлять запрос на другие ноды. Таким образом мы получаем доступность, но теряем консистентность.
   2. P - из-за того, что при выходе отдельной ноды из строя, мы можем обратиться к другой ноде за данными. 
3. ArenadataDB - основана на Greenplum, т.е. архитектура состоит из сегментов PostgreSQL отсюда возникает CA
   1. C - из-за того, что есть master nodes и все сегменты между собой согласованы
   2. A - из-за зеркал сегментов и резервной master ноды


Источники:
1. CAP теорема:
   1. https://www.bigdataschool.ru/wiki/cap
   2. https://habr.com/ru/post/328792/
   3. https://habr.com/ru/post/130577/
2. Dragonfly:
   1. https://dragonflydb.io/
   2. https://habr.com/ru/company/yandex_praktikum/blog/568616/
3. ScyllaDb:
   1. https://habr.com/ru/company/stm_labs/blog/669270/
   2. https://www.scylladb.com/
   3. https://www.nixp.ru/news/13589.html
4. ArenadataDB:
   1. https://docs.arenadata.io/adb/index.html
   2. https://habr.com/ru/company/tinkoff/blog/267733/
   3. https://www.youtube.com/watch?v=B3X7Pw-6Ucc