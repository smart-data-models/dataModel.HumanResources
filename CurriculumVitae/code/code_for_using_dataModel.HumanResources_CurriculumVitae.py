
#         # The code for installing different versions of context brokers are located after the code 
#         
from pysmartdatamodels import pysmartdatamodels as sdm
import subprocess
serverUrl = "http://localhost:1026" # supposed that your broker is installed in localhost with 1026 as default port. Edit to match your configuration
dataModel = "CurriculumVitae"
subject = "dataModel.HumanResources"
settings = {'language': 'ES', 'lastUpdate': '2022-02-28'}
attribute = "settings"
value = settings
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

aboutMe = {'profile': {'name': 'David', 'surnames': 'Bonilla Fuertes', 'title': 'Fundador en Manfred / C-Level Executive', 'description': 'Llevo casi dos décadas desarrollando software, ocupando puestos a lo largo de toda la cadena de valor -programacion, diseño de producto, marketing, ventas y gestión de equipos, departamentos y empresas- pero creo que el rol donde se cruzan mi vocación, mis habilidades y las necesidades de la mayoría de las empresas es en la gestión de equipos y proyectos de construcción de activos digitales.\n\nMe apasiona contribuir en todo el ciclo de vida de un producto o servicio informático, desde la definición hasta el mantenimiento o soporte a clientes, y también involucrarme en la comercialización del mismo.\n\nMe gusta trabajar con gente y para la gente. Como responsable de equipos, mi principal prioridad siempre es eliminar cualquier problema que les impida alcanzar todo su potencial. También procuro devolver a la Comunidad informática parte del valor y el conocimiento que me han aportado a lo largo de mi carrera profesional, dando charlas o colaborando con grupos de usuarios y conferencias técnicas; y, a veces, organizándolos.\n', 'avatar': {'alt': 'foto de David Bonilla', 'link': 'https://pbs.twimg.com/profile_images/1387692137664458758/-Z8bTzmY_400x400.jpg'}, 'birthday': '1977-07-26'}, 'relevantYearsOfExperience': 20, 'relevantLinks': [{'type': 'linkedin', 'URL': 'https://www.linkedin.com/in/dbonillaf/', 'description': 'Mi perfil en LinkedIn'}, {'type': 'twitter', 'URL': 'https://twitter.com/david_bonilla', 'description': 'Mi cuenta de Twitter'}, {'type': 'github', 'URL': 'https://github.com/dbonillaf', 'description': 'Mi cuenta en GitHub'}, {'type': 'website', 'URL': 'https://bonillaware.com/', 'description': 'Mi Blog'}, {'type': 'other', 'URL': 'https://www.bonilista.com', 'description': 'Mi Newsletter'}], 'significativeRelationships': [{'name': 'Diego', 'surnames': 'Arrola', 'title': 'Fundador y General Partner del fondo de capital-riesgo K Fund', 'description': 'Me aporta información sobre el ecosistema startup desde el punto de vista del inversor.', 'contact': {'publicProfiles': [{'type': 'linkedin', 'URL': 'https://www.linkedin.com/in/inakiarrola'}, {'type': 'other', 'URL': 'https://twitter.com/arrola'}]}}, {'name': 'Diego', 'surnames': 'Mariño', 'title': 'Fundador de Ducksboard y antiguo Principal Product Manager en New Relic', 'description': 'Amigo con el que siempre valido ideas y estrategias de Product Management.\n', 'contact': {'publicProfiles': [{'type': 'linkedin', 'URL': 'https://www.linkedin.com/in/diegomarino'}]}}, {'name': 'Alberto', 'surnames': 'Molpeceres', 'title': 'Fundador de Devengo', 'description': 'Consulto habitualmente su opinión sobre decisiones importantes a nivel de ejecución y gestión de operaciones.', 'contact': {'publicProfiles': [{'type': 'linkedin', 'URL': 'https://www.linkedin.com/in/molpe'}]}}], 'interestingFacts': [{'topic': 'First computer', 'fact': 'Amstrad CPC 464'}, {'fact': 'Formar parte del equipo que implementó la **pasarela de pago** online del BBVA Definir, diseñar, desarrollar y lanzar un **ERP** y un **WMS** completos, desde cero, en sólo siete años.'}, {'fact': 'Trabajar como **evangelista técnico** en una prometedora startup australiana y dejarla cuando estaba a punto de empezar a cotizar en el NASDAQ, triplicando las ventas en los territorios a mi cargo para contribuir al éxito colectivo.'}, {'fact': 'Lanzar una campaña de **captación de talento técnico** y conseguir atraer a cientos de personas a Madrid para las pruebas de selección y cobertura en TV.'}, {'fact': 'Fundar una **startup** y cerrar una ronda de 330.000€ de inversión de capital-riesgo.'}, {'fact': 'Concebir, desarrollar y lanzar dos productos web que llegaron a transaccionar €1M anuales en **ventas afiliadas**. Vender ambos y gestionar todo el proceso legal previo y posterior.'}, {'fact': 'Enviar una **newsletter** sobre tecnología, todos los domingos desde hace más de seis años, que más de 15.000 personas quieren recibir.'}, {'fact': 'Organizar un evento anual sobre tecnología que vende todas sus entradas en unos pocos segundos.'}, {'fact': 'Ser **CEO** de una compañía fundada por otros.'}, {'fact': 'Gestionar la implementación y cumplimiento de la **LOPD** y el **RGPD**.'}, {'fact': 'Completar todos los trámites legales, operativos y fiscales necesarios para abrir la filial de una compañía multinacional en Bilbao.'}, {'topic': '¿Cuáles son tus principales herramientas de trabajo (IDEs, editores de texto, clientes de correo, Excel...) y cómo las utilizas (plugins, configuraciones, trucos)?', 'fact': 'Organizo mi tareas personales con **Passion Planner** (un sistema offline) y las profesionales con **Jira** y **Trello**.Tengo tableros compartidos con distintos equipos de trabajo. Uso labels y fechas de entrega para priorizar mi trabajo.\n\nProgramo HTML/CSS/JavaScript con **Visual Studio Code**. Uso algunas extensiones como ‘GitHistory’, ‘Paste JSON as Code’, o ‘Bookmarks’, pero tanto el trabajo con **Git** como la construcción y la construcción con **Gulp** me gusta hacerlo por línea de comandos.\n\nTambién uso bastante **Postman**, además de para hacer pruebas, directamente como interfaz para APIs REST que tengo en producción.'}, {'topic': '¿Qué recursos online (webs, blogs, apps, foros, etc) usas para ayudarte a desempeñar tu trabajo?', 'fact': 'Para informarme de lo más relevante del sector, uso bastante **Twitter** y tengo varias listas específicas por temas. También leo regularmente [Hacker News](https://news.ycombinator.com/) y [Increment](https://increment.com/) y escucho podcasts como[Más que Startups](https://masquestartups.com/).\n\nSi me atasco con algo de código suelo googlear bastante, no tengo un sitio de referencia al que ir, pero muchas veces acabo -supongo que como todos- en [StackOverflow](https://stackoverflow.com/).\n\nPertenezco a un canal de Slack llamado **‘Camaradas del Metal’** donde unas pocas decenas de personas con bastante experiencia suelen comentar y dar contexto a las noticias relacionadas con el emprendimiento tecnológico.'}, {'topic': '¿Qué nuevas tecnologías y/o herramientas te llaman especialmente la atención y por qué?', 'fact': 'Soy muy fan de **Git**, no sólo aplicado al código sino prácticamente a cualquier trabajo colaborativo como documentación o contratos.\n\nMe gusta mucho todo el Ecosistema JavaScript que va más allá del navegador (**React**, **Node**) porque me permite trabajar desde el interfaz a la base de datos (con MongoDB) con la misma sintaxis.\n\nTambién me interesa mucho las posibilidades que puede aportar **Blockchain** para cambiar por completo y democratizar el acceso a según qué sectores y nichos, antes vetados a unos pocos.'}, {'topic': '¿Hay alguna empresa tecnológica que te llame la atención por lo bien que lo está haciendo?', 'fact': 'Creo que [Microsoft](https://www.microsoft.com/es-es/) está dando los pasos correctos para crear todo un sistema de tooling y despliegue que puede atraer a los programadores.\n\nTambién me gusta todo lo que está construyendo [GitLab](https://about.gitlab.com/) y como lo está vendiendo, con una gran documentación y muchísima transparencia.'}, {'topic': '¿Cómo intentas mantener actualizados tus conocimientos y habilidades profesionales?', 'fact': 'Leo todo lo que puedo, pero sobre todo intento hacer pequeños *side projects* que me ayuden a automatizar tareas repetitivas o especialmente pesadas.'}, {'topic': '¿Sueles compartir tu conocimiento por algún canal (posts, foros, contribución a open source, charlas públicas etc)?', 'fact': 'Tengo una lista de correo llamada la [Bonilista](https://www.bonilista.com/) en la que escribo un artículo semanal sobre mis experiencias o temas que me interesan. También organizo —junto a más voluntarios— un evento anual sobre construcción de productos/proyectos digitales llamado [Tarugoconf](https://www.tarugoconf.com/) y suelo participar en distintas conferencias y grupos de usuarios.'}], 'recommendations': [{'title': 'High Output Management', 'type': 'reading', 'authors': [{'name': 'Andrew S.', 'surnames': 'Grove', 'title': 'Former Chairman and CEO of Intel'}], 'summary': 'Un buen manual sobre cómo organizar el trabajo y dirigir equipos para responsables de todos los niveles.'}]}
attribute = "aboutMe"
value = aboutMe
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

experience = {'jobs': [{'organization': {'name': 'Manfred', 'description': 'Plataforma de Talento y agencia de recruiting técnico', 'URL': 'https://www.getmanfred.com/', 'image': {'alt': 'Logo de Manfred', 'link': 'https://pbs.twimg.com/profile_images/946845160004112384/ap8_xjIa_400x400.jpg'}, 'address': {'addressCountry': 'ES', 'addressRegion': 'Madrid', 'addressLocality': 'Madrid', 'postalCode': '28034', 'streetAddress': 'Labastida 1'}}, 'type': 'startup', 'roles': [{'name': 'Fundador', 'startDate': '2018-06-20', 'challenges': [{'description': 'Adaptación de la organización y procesos de la empresa para escalar las operaciones de la misma.', 'actions': ['Implementación de la Holocracia como sistema de gestión.', 'Optimización de los procesos de hiring']}, {'description': 'Desarrollo de producto propio para escalar las operaciones de la compañía, especialmente la aportación de valor a candidatos.', 'actions': ['Definición de visión y alcance de producto.', 'Definición de primer roadmap.', 'Validación de la implementación de funcionalidades.']}, {'description': 'Culminación del [proceso de compraventa](https://bonillaware.com/manfred-sngular) de la compañía por parte de Sngular, manteniendo el núcleo de empleados de la compañía y sin que la productividad o las ventas se resintieran antes, durante y después del mismo.'}, {'description': 'Creación y publicación de contratos open source (candidatos y empresas) para construir un marco legal para una empresa de recruiting.', 'actions': ['Definición de alcance y condiciones de contratos para empresas y representados', 'Gestión del repositorio en GitHub para permitir su publicación y consulta así como potenciales pull requests.']}, {'description': 'Definición del modelo de datos y los procesos necesarios para identificar, clasificar y gestionar perfiles de profesionales técnicos.', 'actions': ['Proceso de onboarding de representados.', 'Perfilado de candidatos', 'Presentación de representados a potenciales empleadores', 'Recepción de ofertas de empleadores']}, {'description': 'Definición de formato CV extendido.', 'actions': ['Definición de estructura de CV optimizado para búsqueda', 'Creación de plantilla y ejemplos']}, {'description': 'Definición e implementación de la web de la compañía.', 'actions': ['Definición de interfaces', 'Redacción de Copy', 'Implementación de copy y links definitivos en el HTML base']}, {'description': 'Apertura de nueva filial en Bilbao.', 'actions': ['Definición de interfaces', 'Redacción de Copy', 'Implementación de copy y links definitivos en el HTML base']}], 'competences': [{'name': 'Balsamiq Mockups', 'type': 'tool', 'description': 'An app to create low-fi definitions of interfaces'}, {'name': 'Atlassian Confluence', 'type': 'tool'}, {'name': 'Atlassian JIRA', 'type': 'tool'}, {'name': 'GitHub', 'type': 'tool'}, {'name': 'BitBucket', 'type': 'tool'}, {'name': 'AWS', 'type': 'tool'}, {'name': 'Airtable', 'type': 'tool'}, {'name': 'GoogleDocs', 'type': 'tool'}, {'name': 'Trello', 'type': 'tool'}, {'name': 'Nginx', 'type': 'tool'}, {'name': 'Gulp', 'type': 'tool'}, {'name': 'VisualStudio Code', 'type': 'tool'}, {'name': 'Basecamp', 'type': 'tool'}, {'name': 'Less', 'type': 'technology'}, {'name': 'NodeJS', 'type': 'technology'}, {'name': 'React', 'type': 'technology'}, {'name': 'Git', 'type': 'technology'}], 'referrals': [{'name': 'Jose Luis', 'surnames': 'Vallejo', 'title': 'Presidente de SNGULAR', 'contact': {'publicProfiles': [{'type': 'linkedin', 'URL': 'https://www.linkedin.com/in/jlvallejo/'}]}}, {'name': 'Yago', 'surnames': 'Cousiño Estevez', 'title': 'Primer empleado de Manfred', 'contact': {'publicProfiles': [{'type': 'linkedin', 'URL': 'https://www.linkedin.com/in/yago-cousi%C3%B1o-13533261/'}], 'contactMails': ['yago@getmanfred.com']}}]}]}, {'organization': {'name': 'Comalatech', 'description': 'Herramientas para facilitar el trabajo colaborativo en el ecosistema de Atlassian Confluence.', 'URL': 'https://www.comalatech.com/', 'image': {'alt': 'Logo de Comalatech', 'link': 'https://www.comalatech.com/wp-content/themes/comalatech/images/comalatech_logo.png?v=1.0.1'}, 'address': {'addressCountry': 'CA', 'addressRegion': 'British Columbia', 'addressLocality': 'Vancouver'}}, 'type': 'startup', 'roles': [{'name': 'CEO', 'startDate': '2017-02-01', 'finishDate': '2018-06-30', 'challenges': [{'description': 'Adaptación de todos los procesos de la compañía al nuevo RGPD', 'actions': ['Definición de requisitos mínimos.', 'Definición de plantillas a cumplimentar por cada nuevo proceso.', 'Documentación de la adecuación de proveedores al reglamento.', 'Definición de la estrategia de petición de consentimiento a usuarios (actuales y nuevos).', 'Redacción de borradores de documentos legales previos a la revisión por departamento legal.']}, {'description': 'Apertura de nueva filial en Bilbao', 'actions': ['Documentación y propuesta para aprovechar las ventajas del régimen fiscal y normativo local.', 'Reuniones con Administraciones locales (Diputación y Gobierno Vasco) para alcanzar acuerdos de colaboración previos al establecimiento.', 'Selección y contratación de los primeros empleados.', 'Búsqueda de oficina representativa, adecuación y reforma de la misma.', 'Búsqueda de proveedores locales (fiscalidad y legal)']}, {'description': 'Coordinación de actividades en Europa', 'actions': ['Gestión de personal (contrataciones, finiquitos, incidencias).', 'Establecimiento de centro logístico para materiales de marketing en España.', 'Gestión de la producción de materiales de marketing para distintos eventos.']}, {'description': 'Estandarización de contratos', 'actions': ['Diseño de políticas retributivas y condiciones laborales comunes para la plantilla en Canadá y España.', 'Negociación individual con cada uno de los empleados para la aceptación de las nuevas condiciones.']}, {'description': 'Soporte'}, {'description': 'Lanzamiento de Comala Agile Ranking'}], 'competences': [{'name': 'Basecamp', 'type': 'tool'}, {'name': 'Atlassian Confluence', 'type': 'tool'}, {'name': 'Atlassian JIRA', 'type': 'tool'}, {'name': 'BlueJeans Videoconference', 'type': 'tool'}], 'referrals': [{'name': 'Gorka', 'surnames': 'Puente', 'title': 'Group Product Manager en Comalatech', 'contact': {'publicProfiles': [{'type': 'linkedin', 'URL': 'https://www.linkedin.com/in/gorkapuente/'}]}}]}]}, {'organization': {'name': 'Instituto de Empresa'}, 'type': 'academicalInstitution', 'roles': [{'name': 'Profesor asociado de productividad y metodologías ágiles', 'startDate': '2015-04-12'}]}], 'publicArtifacts': [{'details': {'name': 'JSON Schema: dotando a tus datos de un formato y a tus APIs de un contrato | T3chFest 2019', 'URL': 'https://www.youtube.com/watch?v=KB2DkeQo8d8'}, 'type': 'talk', 'publishingDate': '2019-03-22', 'relatedCompetences': [{'name': 'JSON', 'type': 'technology'}, {'name': 'recruiting', 'type': 'domain'}], 'tags': ['keynotes', 'youtube', 't3chfest']}, {'details': {'name': 'Tarugoconf', 'description': 'Organizador del evento más gallego y awesómico del mundo.', 'URL': 'https://www.tarugoconf.com/', 'image': {'alt': 'Logo de la Tarugoconf', 'link': 'https://www.tarugoconf.com/img/logo-tarugo.png'}}, 'type': 'sideProject'}]}
attribute = "experience"
value = experience
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

knowledge = {'languages': [{'name': 'ES', 'fullName': 'Español', 'level': 'Native or bilingual proficiency'}, {'name': 'EN', 'level': 'Full professional proficiency'}, {'name': 'GL', 'level': 'Elementary proficiency'}], 'hardSkills': [{'skill': {'name': 'JIRA', 'type': 'tool', 'description': 'Administración, configuración y gestión avanzada de JIRA.'}, 'level': 'expert'}, {'skill': {'name': 'JAVA', 'type': 'technology'}, 'level': 'high'}], 'softSkills': [{'skill': {'name': 'Liderazgo', 'type': 'practice', 'description': 'Liderar equipos/organizaciones para que alcancen los objetivos marcados, en tiempo y presupuesto, sin incrementar la rotación de personal.'}, 'level': 'expert'}, {'skill': {'name': 'Atraer talento y retenerlo', 'type': 'practice'}, 'level': 'expert'}, {'skill': {'name': 'Orientado a resultados', 'type': 'practice', 'description': 'Acabar proyectos, además de empezarlos.'}, 'level': 'expert'}, {'skill': {'name': 'Comunicación', 'type': 'practice', 'description': 'Comunicar lo que hago, cómo lo hago y -sobre todo- por qué lo hago, tanto de forma oral como escrita, con cierta efectividad.'}, 'level': 'expert'}, {'skill': {'name': 'Logística', 'type': 'domain', 'description': 'Conocimientos avanzados de aprovisionamiento, almacenamiento, gestión y distribución de bienes'}, 'level': 'high'}], 'studies': [{'studyType': 'officialDegree', 'degreeAchieved': False, 'name': 'Ingeniería Técnica Informática', 'description': 'Computer Science Grade', 'startDate': '2002-09-15', 'finishDate': '2006-06-30', 'institution': {'name': 'UOC', 'description': 'Universitat Oberta de Catalunya', 'URL': 'https://www.uoc.edu/', 'image': {'alt': 'logo de UOC', 'link': 'https://upload.wikimedia.org/wikipedia/commons/1/1b/Logo_UOC.svg'}, 'address': {'addressCountry': 'ES', 'addressRegion': 'Cataluña', 'notes': 'Universidad a distancia'}}}, {'studyType': 'certification', 'degreeAchieved': True, 'name': 'Master en Desarrollo de Aplicaciones Web', 'description': 'Computer Science Grade', 'startDate': '2000-09-15', 'finishDate': '2001-06-30', 'institution': {'name': 'CFDTI IBM/La Caixa', 'description': 'Centro de Formación de Desarrollo de Tecnologías Informáticas una joint venture de IBM y La Caixa que, desgraciadamente, no perduró en el tiempo.', 'address': {'addressCountry': 'ES', 'addressRegion': 'Madrid', 'addressLocality': 'Madrid'}}}, {'studyType': 'certification', 'degreeAchieved': True, 'name': 'Certified Scrum Master', 'description': 'Scrum Master certificado por la Scrum Alliance', 'startDate': '2007-05-14', 'finishDate': '2007-05-21', 'institution': {'name': 'Scrum Alliance', 'description': 'Curso de certificación impartido por Ariel Ber', 'address': {'addressCountry': 'ES', 'addressRegion': 'Madrid', 'addressLocality': 'Madrid'}}}]}
attribute = "knowledge"
value = knowledge
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

print(" In case you have installed the a cntext broker (see comments below )")
print(" Execute this instruction to check that the entities has been inserted")
command = ['curl', '-X', 'GET', 'http://localhost:1026/ngsi-ld/v1/entities?local=true&limit=1000']
result = subprocess.run(command, capture_output=True, text=True)
print(result.stdout)

#         This code allows you to install different context brokers in a linux system
#        
#         # ORION-LD 
#         # The manuals are here https://github.com/FIWARE/context.Orion-LD/tree/develop/doc/manuals-ld
#         
#         # INSTALL NGSI LD broker (OrionLD)
#         sudo docker pull mongo:3.6
#         sudo docker pull fiware/orion-ld
#         sudo docker network create fiware_default
#         sudo docker run -d --name=mongo-db --network=fiware_default --expose=27017 mongo:3.6 --bind_ip_all --smallfiles
#         sudo docker run -d --name fiware-orionld -h orion --network=fiware_default -p 1026:1026  fiware/orion-ld -dbhost mongo-db
#         
#         # TO RELAUNCH (only if you have already installed a broker in the same machine)
#         sudo docker stop fiware-orionld
#         sudo docker rm fiware-orionld
#         sudo docker stop mongo-db
#         sudo docker rm mongo-db
#         sudo docker network rm fiware_default
#         
#         # CHECK INSTANCES
#         # Check the broker is running
#         curl -X GET 'http://localhost:1026/version'
#         
#         # Check what entities are in the broker
#         curl -X GET http://localhost:1026/ngsi-ld/v1/entities?local=true&limit=1000
#         
#        # STELLIO
#        
#        # INSTALL NGSI LD broker (Stellio)
#        curl -O https://raw.githubusercontent.com/stellio-hub/stellio-context-broker/develop/docker-compose.yml -O https://raw.githubusercontent.com/stellio-hub/stellio-context-broker/develop/.env
#        curl -o config/kafka/update_run.sh --create-dirs https://raw.githubusercontent.com/stellio-hub/stellio-context-broker/develop/config/kafka/update_run.sh && chmod u+x config/kafka/update_run.sh
#        docker compose up -d
#        # wait for some seconds for services to be up and running
# 
#        # TO RELAUNCH (only if you have already installed a broker in the same machine)
#        docker compose down
# 
#        # CHECK INSTANCES
#        curl -X GET 'http://localhost:8080/actuator/health'
#        curl -X GET 'http://localhost:8080/search-service/actuator/health'
# 
#        # view the logs
#        docker-compose logs -f --tail=100
#        
#        # SCORPIO
#        sudo docker pull postgis/postgis
#        sudo docker pull scorpiobroker/all-in-one-runner:java-latest
#        sudo docker network create fiware_default
#        sudo docker run -d --name postgres --network=fiware_default -h postgres -p 5432 -e POSTGRES_USER=ngb -e POSTGRES_PASSWORD=ngb -e POSTGRES_DB=ngb postgis/postgis
#        sudo docker run -d --name scorpio -h scorpio --network=fiware_default -e DBHOST=postgres -p 9090:9090  scorpiobroker/all-in-one-runner:java-latest
#         
#          # TO RELAUNCH (only if you have already installed a broker in the same machine)
#        sudo docker stop scorpio
#        sudo docker rm scorpio
#        sudo docker stop postgres
#        sudo docker rm postgres
#        sudo docker network rm fiware_default
#         
#          # CHECK INSTANCES
#          # Check the broker is running
#                                # Release Info
#        curl -X GET 'http://localhost:9090/q/info'
#          # Health status of the broker
#        curl -X GET 'http://localhost:9090/q/health'
#         
#         # Check what entities are in the broker
#         curl -X GET http://localhost:1026/ngsi-ld/v1/entities?local=true&limit=1000
#        
#        
#         # now the python code you can use to insert some value in the context broker according to the data model
#         # Version Warning! 
#         # This code is designed to work with the version 0.8.0.1 of pysmartdatamodels or later
# 
#         
#         