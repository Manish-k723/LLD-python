from Notification.notification_priority import NotificationPriority


class Template:
    def __init__(self, name: str, body: str):
        self._name = name
        self._body = body

    def render(self, **context: str) -> str:
        return self._body.format(**context)

    def get_name(self) -> str:
        return self._name


class TemplateService:
    def __init__(self):
        self._templates = {
            "basic": Template("basic", "Hi {recipient_name}, {message}"),
            "alert": Template("alert", "Important update for {recipient_name}: {message}"),
            "campaign": Template("campaign", "Hello {recipient_name}! {message}"),
        }

    def get_template(
        self,
        priority: NotificationPriority,
        template_name: str | None = None,
    ) -> Template:
        if template_name and template_name in self._templates:
            return self._templates[template_name]
        if priority == NotificationPriority.CRITICAL:
            return self._templates["alert"]
        if priority == NotificationPriority.NON_CRITICAL:
            return self._templates["campaign"]
        return self._templates["basic"]
