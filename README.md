# 🚀 АГЕНТ ДЛЯ МОНИТОРИНГА СЕТЕВОГО ТРАФИКА

Простой агент мониторинга сетевого трафика с возможностью детектирования посещения определённых сайтов.  
Данные логируются в JSON-файл и отправляются в Elasticsearch через Filebeat для последующей визуализации в Kibana.

---

## 🧩 Описание

Этот Python-скрипт работает как **локальный SIEM-агент** на Windows и делает следующее:

- Мониторит активные TCP-соединения
- Получает домены из IP-адресов (через обратный DNS)
- Проверяет, является ли домен "триггерным" (например, `vk.com`)
- Логирует события в JSON-файл
- Поддерживает интеграцию с ELK (Elasticsearch + Kibana) через Filebeat
- Можно использовать как основу для расширения (HTTPS, MITM, GUI)

---

## 📁 Структура проекта

```
siem_agent/
├── agent/
│   ├── __init__.py
│   ├── config.py                # Конфиг: триггерные домены
│   ├── network_monitor.py       # Мониторинг соединений
│   ├── trigger_handler.py       # Проверка триггеров
│   ├── logger.py                # Логирование событий
│   └── main.py                  # Точка входа
├── data/
│   └── logs/
│       └── traffic_logs.json    # Логи событий
├── config/
│   └── domains.yaml             # Список триггерных доменов
├── utils/
│   └── helpers.py               # Вспомогательные функции
├── install.bat                  # Установка зависимостей
├── run.bat                      # Запуск агента
├── requirements.txt             # Зависимости Python
└── README.md                    # Этот файл
```

---

## 🧰 Технологии

| Технология      | Назначение |
|----------------|------------|
| Python 3.10     | Основной язык разработки |
| psutil          | Чтение сетевых соединений |
| scapy           | Альтернатива для сниффинга трафика |
| PyYAML          | Работа с конфигами |
| Elasticsearch   | Хранение и индексация логов |
| Kibana          | Визуализация данных |
| Filebeat        | Передача логов в Elasticsearch |

---

## 🔧 Установка и запуск

### 1. Установи зависимости

```bash
pip install -r requirements.txt
```

> Для работы `scapy` на Windows установи Npcap: https://nmap.org/npcap/

---

### 2. Настрой Filebeat

Создай или обнови `filebeat.yml`:

```yaml
filebeat.inputs:
  - type: filestream
    enabled: true
    id: siem-agent-json-logs
    paths:
      - D:\siem_agent\data\logs\traffic_logs.json
    json.keys_under_root: true
    json.add_error_key: true

output.elasticsearch:
  hosts: ["http://localhost:9200"]
  index: "siem-agent-%{+yyyy.MM.dd}"

setup.kibana:
  host: "http://localhost:5601"
```

Запусти Filebeat:

```powershell
.\filebeat.exe -e -c filebeat.yml
```

---

### 3. Запустите агент

```powershell
cd agent
python main.py
```

или используй `.bat`:

```bat
@echo off
cd /d "%~dp0%"
python main.py
```

---

## 📌 Как работает агент

1. **network_monitor.py** — отслеживает TCP-соединения через `psutil`.
2. **trigger_handler.py** — проверяет, есть ли домен в списке триггеров.
3. **logger.py** — записывает событие в JSON-файл с полями:
   ```json
   {
     "timestamp": "2025-05-17T12:00:00",
     "domain": "vk.com",
     "triggered": true,
     "event": {
       "category": "security",
       "type": "alert"
     },
     "user": "admin"
   }
   ```
4. **Filebeat** считывает JSON-файл и отправляет его в **Elasticsearch**.
5. **Kibana** предоставляет интерфейс для анализа и визуализации.

---

## 🛡️ Пример использования в Kibana

1. Перейди в **Analytics → Discover**
2. Используй фильтры:

```kql
event.category : "security"
```

или

```kql
message:"event" AND message:"security"
```

3. Создай дашборд в **Analytics → Dashboard**

---

## 🧪 Возможности расширения

- Добавление HTTPS-мониторинга
- Парсинг URL из HTTP-заголовков
- Интеграция с Windows Event Log
- Графический интерфейс (Tkinter / PyQt)
- Отправка уведомлений (Telegram, Email)
- Автономная установка как службы Windows

---

## ✅ Полезные команды

| Команда                          | Что делает |
|----------------------------------|------------|
| `python main.py`                 | Запуск агента |
| `curl http://localhost:9200`     | Проверка Elasticsearch |
| `curl http://localhost:5601`     | Проверка Kibana |
| `netstat -ano`                  | Проверка портов |

---


## 🙌 Автор

*Mara Chedder*  
Дата: 2025-05-17  
Проект: SIEM-агент для Windows

---
