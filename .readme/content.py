"""Every word the profile prints, in English and Spanish.

Knowledge only: no employers, clients, dates or metrics. Code in the drawing stays in English in both languages.
"""

EMAIL = "afzar27@gmail.com"
SITE = "https://www.andres-zapata.dev/"
LINKEDIN = "https://www.linkedin.com/in/andres-zapata-aristizabal/"
RAW = "https://raw.githubusercontent.com/AZapata27/AZapata27/main/assets/"

TEXT = {
    "en": {
        "subtitle": "Software architect, 10+ years. Fintech, banking, logistics and transportation, integrations.",
        "subtitle_m": ["Software architect, 10+ years. Fintech, banking,", "logistics and transportation, integrations."],
        "bus": "teams · 200+ people led · AI trainings",
        "bus_m": "teams · 200+ led · AI trainings",
        "problem": "your problem",
        "router": "content-based router",
        "aggregator": "aggregator",
        "production": "production",
        "branches": [("ARCHITECTURE", "translator", "AWS · Azure · GCP · DDD · events", 1),
                     ("INTEGRATION", "route", "EIP · Camel · Quarkus · Kafka", 2),
                     ("AI-NATIVE DEVELOPER", "agent", "harness · MCP · skills · agents", 3)],
        "title_rows": [("DRAWING", "andres-zapata.route", None), ("ROLE", "Software architect", None),
                       ("EXPERIENCE", "10+ years", None), ("DOMAINS", "fintech · banking", None),
                       ("", "logistics · transportation", None), ("SCOPE", "integrations", None),
                       ("LET'S TALK", EMAIL, "talk"), ("LINKS", "GitHub|LinkedIn|Portfolio", "links")],
        "write_me": "WRITE ME",
        "hero_title": "Andrés Zapata, integration route",
        "hero_desc": ("Andrés Zapata, software architect, 10+ years: fintech, banking, logistics and transportation, "
                      "integrations. Drawn as an Enterprise Integration Patterns route: your problem enters an inbound "
                      "channel, a content-based router sends it to architecture (AWS, Azure, GCP, DDD, events), "
                      "integration (EIP, Camel, Quarkus, Kafka) or AI-native development (harness, MCP, skills, agents), "
                      "an aggregator joins the branches and the result goes to production. Leadership and AI trainings "
                      f"run as the control bus. Let's talk: {EMAIL}. Links: GitHub, LinkedIn, portfolio."),
        "notes_title": "NOTES",
        "notes": [
            (1, "ARCHITECTURE",
             "Cloud-native designs on AWS, Azure and GCP. DDD, event-driven, observable from day one, load- and "
             "chaos-tested before shipping. Ten years across fintech, banking, logistics and transportation."),
            (2, "INTEGRATION",
             "Expertise in enterprise integration: Enterprise Integration Patterns with Apache Camel on Quarkus, and "
             "event streaming with Kafka Connect, Debezium and Kafka Streams."),
            (3, "AI-NATIVE DEVELOPER",
             "AI is in every step: spec, design, code, review, release. I build agent harnesses, MCP servers, skills, "
             "agents, and the governance that lets a company trust them. Claude Code, the Anthropic and OpenAI APIs, "
             "LangChain, MCP and Hugging Face."),
            (4, "CONTROL BUS",
             "More than 200 people led over the last five years. I coach developers into senior and architect roles "
             "and run corporate AI trainings, so a whole team can work this way."),
        ],
        "parts_title": "PARTS LIST",
        "parts_cols": ("ITEM", "GROUP", "PARTS"),
        "stack": [
            ("AI", ["claude", "openai", "langchain", "mcp", "huggingface"],
             "Claude Code, Anthropic and OpenAI APIs, LangChain, Model Context Protocol, Hugging Face"),
            ("LANGUAGES", ["java", "kotlin", "typescript", "javascript", "go"],
             "Java, Kotlin, TypeScript, JavaScript, Go"),
            ("BACKEND", ["spring", "quarkus", "camel", "nodejs", "nestjs"],
             "Spring Boot, WebFlux, Quarkus, Apache Camel, Vert.x, Node.js, NestJS"),
            ("FRONTEND", ["angular", "react", "vuejs", "nextjs"], "Angular, React, Vue, Next.js"),
            ("DATA AND EVENTS", ["apachekafka", "postgresql", "oracle", "mongodb", "redis", "dynamodb"],
             "Kafka (Confluent), Debezium, GCP Pub/Sub, PostgreSQL, Oracle, MongoDB, Redis, DynamoDB"),
            ("CLOUD AND DEVOPS", ["amazonwebservices", "googlecloud", "azure", "redhatopenshift", "kubernetes",
                                  "docker", "terraform", "githubactions", "keycloak", "kong"],
             "AWS, GCP, Azure, OpenShift, Kubernetes, Docker, Terraform, GitHub Actions, Keycloak, Kong"),
            ("OBSERVABILITY", ["opentelemetry", "prometheus", "grafana"],
             "OpenTelemetry, Prometheus, Grafana, Loki, Tempo"),
            ("QUALITY", ["junit", "cypressio", "k6", "sonarqube"],
             "JUnit, Testcontainers, Cypress, k6, Gatling, chaos engineering, SonarQube"),
        ],
        "buttons": [("link-mail", "let's talk", f"mailto:{EMAIL}", f"Let's talk: {EMAIL}"),
                    ("link-site", "andres-zapata.dev", SITE, "andres-zapata.dev"),
                    ("link-linkedin", "linkedin", LINKEDIN, "LinkedIn")],
        "notes_desc_prefix": "Notes.",
        "parts_desc_prefix": "Parts list.",
    },
    "es": {
        "subtitle": "Arquitecto de software, 10+ años. Fintech, banca, logística y transporte, integraciones.",
        "subtitle_m": ["Arquitecto de software, 10+ años. Fintech, banca,", "logística y transporte, integraciones."],
        "bus": "equipos · 200+ personas lideradas · formación en IA",
        "bus_m": "equipos · 200+ lideradas · IA",
        "problem": "tu problema",
        "router": "router por contenido",
        "aggregator": "agregador",
        "production": "producción",
        "branches": [("ARQUITECTURA", "translator", "AWS · Azure · GCP · DDD · eventos", 1),
                     ("INTEGRACIÓN", "route", "EIP · Camel · Quarkus · Kafka", 2),
                     ("DESARROLLADOR AI-NATIVE", "agent", "harness · MCP · skills · agentes", 3)],
        "title_rows": [("PLANO", "andres-zapata.route", None), ("ROL", "Arquitecto de software", None),
                       ("EXPERIENCIA", "10+ años", None), ("DOMINIOS", "fintech · banca", None),
                       ("", "logística · transporte", None), ("ALCANCE", "integraciones", None),
                       ("HABLEMOS", EMAIL, "talk"), ("ENLACES", "GitHub|LinkedIn|Portafolio", "links")],
        "write_me": "ESCRÍBEME",
        "hero_title": "Andrés Zapata, ruta de integración",
        "hero_desc": ("Andrés Zapata, arquitecto de software, 10+ años: fintech, banca, logística y transporte, "
                      "integraciones. Dibujado como una ruta de Enterprise Integration Patterns: tu problema entra por "
                      "un canal, un router por contenido lo envía a arquitectura (AWS, Azure, GCP, DDD, eventos), "
                      "integración (EIP, Camel, Quarkus, Kafka) o desarrollo AI-native (harness, MCP, skills, agentes), "
                      "un agregador une las ramas y el resultado sale a producción. El liderazgo y la formación en IA "
                      f"funcionan como control bus. Hablemos: {EMAIL}. Enlaces: GitHub, LinkedIn, portafolio."),
        "notes_title": "NOTAS",
        "notes": [
            (1, "ARQUITECTURA",
             "Diseños cloud-native en AWS, Azure y GCP. DDD, orientado a eventos, observable desde el primer día, con "
             "pruebas de carga y de caos antes de salir a producción. Diez años en fintech, banca, logística y "
             "transporte."),
            (2, "INTEGRACIÓN",
             "Experiencia en integración empresarial: Enterprise Integration Patterns con Apache Camel sobre Quarkus, "
             "y streaming de eventos con Kafka Connect, Debezium y Kafka Streams."),
            (3, "DESARROLLADOR AI-NATIVE",
             "IA en cada paso: especificación, diseño, código, revisión y entrega. Construyo agent harnesses, "
             "servidores MCP, skills, agentes y la gobernanza que permite a una empresa confiar en ellos. Claude Code, "
             "las APIs de Anthropic y OpenAI, LangChain, MCP y Hugging Face."),
            (4, "CONTROL BUS",
             "Más de 200 personas lideradas en los últimos cinco años. Acompaño a desarrolladores hacia roles senior y "
             "de arquitectura, y doy formación corporativa en IA para que equipos completos trabajen así."),
        ],
        "parts_title": "LISTA DE PARTES",
        "parts_cols": ("ÍTEM", "GRUPO", "PARTES"),
        "stack": [
            ("IA", ["claude", "openai", "langchain", "mcp", "huggingface"],
             "Claude Code, APIs de Anthropic y OpenAI, LangChain, Model Context Protocol, Hugging Face"),
            ("LENGUAJES", ["java", "kotlin", "typescript", "javascript", "go"],
             "Java, Kotlin, TypeScript, JavaScript, Go"),
            ("BACKEND", ["spring", "quarkus", "camel", "nodejs", "nestjs"],
             "Spring Boot, WebFlux, Quarkus, Apache Camel, Vert.x, Node.js, NestJS"),
            ("FRONTEND", ["angular", "react", "vuejs", "nextjs"], "Angular, React, Vue, Next.js"),
            ("DATOS Y EVENTOS", ["apachekafka", "postgresql", "oracle", "mongodb", "redis", "dynamodb"],
             "Kafka (Confluent), Debezium, GCP Pub/Sub, PostgreSQL, Oracle, MongoDB, Redis, DynamoDB"),
            ("NUBE Y DEVOPS", ["amazonwebservices", "googlecloud", "azure", "redhatopenshift", "kubernetes",
                               "docker", "terraform", "githubactions", "keycloak", "kong"],
             "AWS, GCP, Azure, OpenShift, Kubernetes, Docker, Terraform, GitHub Actions, Keycloak, Kong"),
            ("OBSERVABILIDAD", ["opentelemetry", "prometheus", "grafana"],
             "OpenTelemetry, Prometheus, Grafana, Loki, Tempo"),
            ("CALIDAD", ["junit", "cypressio", "k6", "sonarqube"],
             "JUnit, Testcontainers, Cypress, k6, Gatling, ingeniería del caos, SonarQube"),
        ],
        "buttons": [("link-mail", "hablemos", f"mailto:{EMAIL}", f"Hablemos: {EMAIL}"),
                    ("link-site", "andres-zapata.dev", SITE, "andres-zapata.dev"),
                    ("link-linkedin", "linkedin", LINKEDIN, "LinkedIn")],
        "notes_desc_prefix": "Notas.",
        "parts_desc_prefix": "Lista de partes.",
    },
}


def suffix(lang):
    """English keeps the original file names; Spanish adds `.es` before the extension."""
    return "" if lang == "en" else ".es"
