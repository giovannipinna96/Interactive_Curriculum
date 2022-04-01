import streamlit as st
from PIL import Image


#####################
# Custom function for printing text
def txt(a, b):
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt2(a, b):
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)


def txt3(a, b):
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt4(a, b, c):
    col1, col2, col3 = st.columns([1.5, 2, 2])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)
    with col3:
        st.markdown(c)


def is_section(sections, str):
    try:
        sections.index(str)
        return True
    except:
        return False


with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
#####################
# Header
st.write('''
##### *Resume* 
# Giovanni Pinna, Master Degree
''')
mode = st.radio('Mode', ('Professional', 'Programming'))
# if mode == 'Professional':
#     image = Image.open('professional.png')
#     st.image(image, width=300)
# else:
#     image = Image.open('programmer.png')
#     st.image(image, width=300)

language = st.radio('Language', ('Italiano', 'English'))

if language == 'Italiano':
    sections = st.multiselect('Sections',
                              ['Informazioni', 'Formazione', 'Esperienze lavorative', 'Skills', 'Corsi e Certificati'],
                              default=['Informazioni', 'Formazione', 'Esperienze lavorative', 'Skills',
                                       'Corsi e Certificati'])

    if is_section(sections, 'Informazioni'):
        st.markdown('## Informazioni', unsafe_allow_html=True)
        st.info('''
        - Sono uno studente di ingegneria informatica con una forte passione per la data analysis e l'artificial intelligence.
        - Attualmente sto svolgendo l'attività di tutor dei tirocini presso la mia università e sto svolgendo dei progetti personali di statistica e computer vision.
        - Credo sia importante migliorarsi continuamente sia per quanto riguarda le hard skill che le soft skill. 
          Per migliorare quest'ultime ho deciso di intraprendere dei progetti anche al di fuori del settore dell'informatica il che mi ha portato ad uscire dalla mia comfort zone e apprendere molto nei settori del digital transformation, user experience e economia.
        ''')

    #####################
    # Navigation

    st.markdown(
        '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',
        unsafe_allow_html=True)

    st.markdown("""
    <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #1771A0;">
      <a class="navbar-brand" href="https://giovannipinna.net" target="_blank">Sito Web</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item active">
            <a class="nav-link disabled" href="#resume">Giovanni Pinna</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#formazione">Formazione</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#esperienze-lavorative">Esperienze Lavorative</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#skills">Skills</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#corsi-e-certificati">Corsi e Certificati</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#social-media">Social Media</a>
          </li>
        </ul>
      </div>
    </nav>
    """, unsafe_allow_html=True)

    #####################
    if is_section(sections, 'Formazione'):
        st.markdown('''
        ## Formazione
        ''')
        txt('**Laurea Magistrale** Ingegneria informatica, *Università degli studi di Trieste*, Italia',
            '2019 - presente')
        st.markdown('''
        - Media: `28.0`
        - Appassinatomi al campo della data science e dell'intelligenza artificiale ho deciso di plasmare il mio percorso universitario facendo molte materie in questi ambiti anche offerti da altri enti importanti della mia città (come la scuola di specializzazione SISSA)
        - In questo momento mi sto dedicando a concludere la mia tesi magistrale in materia di computer vision
        ''')

        txt('**Erasmus** , master in logistica *Montanuniversität Leoben*, Austria',
            'settembre 2021 - marzo 2022')
        st.markdown('''
        - Media: `1 -> (equivalente al 30L)`
        - La Montanuniversität Leoben è un importante università a livello europeo e mondiale nei settori del ingegneria mineraria, petrolifera e della logistica
        - Ho scelto questa università per darmi la possibilità di esplorare dei settori nuovi e che in Italia non eseistono. In particolare ho avuto la possibilità di analizzare dati petroliferi e apprendere le principali tecniche che si usano, apprendere qualcosa in più su tutta la parte economica e decisionale che dietro il mondo petrolifero. Infine ho avuto anche la possibilità di capire i principali aspetti della logistica industriale. 
        - Ho deciso di fare lo scambio internazionale malgrado la situazione sanitaria internazionale soprattutto per cambiare ambiente e vivere la vita universitaria e la cultura di un altro paese. Non ho paura di affermare, senza esagerare che è stata una delle più belle e soddisfacienti esperienze della mia vita
        ''')

        txt('**Laurea triennale** in igegneria informatica, *Univeristà degli studi di Trieste*, Italia',
            '2015 - 2018')
        st.markdown('''
        - Tesi triennale in : *Codici LDPC con relazione lineare tra lunghezza della parola e distanza minima: stima dell'upper bound della frame error rate*.
        ''')

        txt('**Diploma superiore** , perito in infomratica e telecomunicazioni *Istituto tecnico Alessando Volta*, Italia',
            '2010 - 2015')
        st.markdown('''
        - Come tesina delle superiori portai un modellino di una casa domotica controllabile da remoto realizata con Arduino.
        ''')

    #####################
    if is_section(sections, 'Esperienze lavorative'):
        st.markdown('''
        ## Esperienze lavorative
        ''')

        txt('**Member**, Contamination LAB, Università degli studi di Trieste, Italia',
            '2020-2021')
        st.markdown('''
        - Il CLab nasce con l'obbiettivo di consentire agli studenti  di sviluppare  la propria idea imprenditoriale con il supporto di docenti e mentori esperti nel settore. 
        - Grazie a questa esperienza ho avuto modo non solo di concretizzare le conoscenze apprese in ambito universitario, ma anche di apprendere nuove tecniche che ritengo mi torneranno utili nel mio futuro lavorativo, come ad esempio, predisporre un business plan e un business model per organizzare al meglio il mio progetto e valutarne le potenzialità. 
        - Frutto di questa esperienza e di mesi di lavoro è "Influence", il mio progetto innovativo che mi auguro di realizzare un giorno. "Influence" rappresenta la perfetta sintesi della mia esperienza al Clab, in quanto concilia il mondo del marketing e dell'intelligenza artificiale. In tal senso, il mio progetto, attraverso lo studio dei dati degli utenti, si propone di creare  contenuti sempre nuovi che soddisfino i mutevoli interessi del pubblico.
        ''')

        txt('**Tutor**, Facoltà di ingegneria e architettura, Università degli studi di Trieste, Italia',
            '2020-2021')
        st.markdown('''
        - Gestito tutto l'ambito riguradante i tirocini e le convenzioni con le aziende del mio dipartimento.
        - Facilitato il contatto tra studenti, aziende e università seguendoli nella procedura per la richiesta di un tirocinio. 
        ''')

        txt('**Help desk di primo livello**, BDF S.p.A, Trieste, Italia',
            'aprile 2019- agosto 2019')

        txt('**Tirocinante informatico**, U_BLOX ITALIA S.p.A., Sgonico, Italia',
            'luglio 2015- settembre 2015')

    #####################
    if is_section(sections, 'Skills'):
        st.markdown('''
        ## Skills
        ''')
        txt3('Programming', '`Python`, `Java`, `C` , `C++` , `SQL`, `VBA` , `Linux`')
        txt3('Data processing', ' `pandas`, `numpy`')
        txt3('Data visualization', '`matplotlib`, `Excel`')  # `seaborn`, `plotly`, `altair`, `ggplot2`
        txt3('Machine Learning', '`scikit-learn`')
        txt3('Deep Learning', '`Pycharm` , `Keras`')
        txt3('Web development', ' `HTML`, `CSS` , `WordPress`')

    #####################
    if is_section(sections, 'Corsi e Certificati'):
        st.markdown('''
        ## Corsi e Certificati
        #### Corsi presso Montanuniversität Leoben
        - Computational Methods and Tools for Logistics
        - Production Data Analysis and Modelling
        - Decision-Making and Risk Analysis
        - Mechatronic Design Project
        - Fundamentals of Logistics Systems Engineering
        
        #### Cosi presso Università degli studi di Trieste
        - Natural language processing
        - Deep learning
        - Computer vision and pattern recognition 
        - Basi di dati
        - Computer networks 2 and introduction to cybersecurity
        - Foundation of high performance computing corso del master in HPC della scuola di specializzazione SISSA
        - Introduction to machine learning and evolutionary robotics
        - Open Data Management and the Cloud in collaborazione con INAF
        - Progettazione del software e dei sistemi operativi
        
        #### Corsi regionali extra
        - Business plan, cos'è e come si usa
        - Busienss model canvas
        - New product forecasting
        - Storytelling e comunicazione
        - Leaderschip, team building and social strategies  
        ''')
else:
    sections = st.multiselect('Sections',
                              ['About me', 'Education', 'Work experiences', 'Skills', 'Courses and certified'],
                              default=['About me', 'Education', 'Work experiences', 'Skills', 'Courses and certified'])
    if is_section(sections, 'About me'):
        st.markdown('## About me', unsafe_allow_html=True)
        st.info('''
         - I am a computer engineering student with a strong passion for data analysis and artificial intelligence.
         - I am currently carrying out the activity of internship tutor at my university and I am carrying out personal statistics and computer vision projects.
         - I think it is important to continuously improve both in terms of hard skills and soft skills.
           To improve the latter I decided to undertake projects also outside the IT sector which led me to leave my comfort zone and learn a lot in the sectors of digital transformation, user experience and economy.
        ''')

    #####################
    # Navigation

    st.markdown(
        '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',
        unsafe_allow_html=True)

    st.markdown("""
     <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #1771A0;">
       <a class="navbar-brand" href="https://giovannipinna.net" target="_blank">Web Site</a>
       <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
         <span class="navbar-toggler-icon"></span>
       </button>
       <div class="collapse navbar-collapse" id="navbarNav">
         <ul class="navbar-nav">
           <li class="nav-item active">
             <a class="nav-link disabled" href="#resume">Giovanni Pinna <span class="sr-only">(current)</span></a>
           </li>
           <li class="nav-item">
             <a class="nav-link" href="#formazione">Education</a>
           </li>
           <li class="nav-item">
             <a class="nav-link" href="#esperienze-lavorative">Work Experiences</a>
           </li>
           <li class="nav-item">
             <a class="nav-link" href="#skills">Skills</a>
           </li>
           <li class="nav-item">
             <a class="nav-link" href="#corsi-e-certificati">Courses and certified</a>
           </li>
           <li class="nav-item">
             <a class="nav-link" href="#social-media">Social Media</a>
           </li>
         </ul>
       </div>
     </nav>
     """, unsafe_allow_html=True)

    #####################
    if is_section(sections, 'Education'):
        st.markdown('''
         ## Education
         ''')
        txt('**Master Degree** Computer sicence engineering, *University of Treiste*, Italy',
            '2019 - present')
        st.markdown('''
         - Mark mean: `28.0`
         - Passionate about the field of data science and artificial intelligence, I decided to shape my university career by doing many subjects in these areas also offered by other important institutions in my city (such as the SISSA specialization school)
         - Right now I'm dedicating myself to finish my master's thesis on computer vision
         ''')

        txt('**Erasmus** , Master in logistic *Montanuniversität Leoben*, Austria',
            'September 2021 - March 2022')
        st.markdown('''
         - Mark mean: `1 -> (equivalent to 30L)`
         - The Montanuniversität Leoben is an important European and world-wide university in the fields of mining, oil and logistics engineering
         - I chose this university to give me the opportunity to explore new sectors that do not exist in Italy. In particular, I had the opportunity to analyze oil data and learn the main techniques that are used, learn something more about the whole economic and decision-making part that is behind the oil world. Finally, I also had the opportunity to understand the main aspects of industrial logistics.
         - I decided to do the international exchange despite the international health situation above all to change the environment and live the university life and culture of another country. I'm not afraid to say, without exaggerating, that it was one of the most beautiful and satisfying experiences of my life.
         ''')

        txt('**Bachelor Degree** Computer science engineering, *University of Treiste*, Italy',
            '2015 - 2018')
        st.markdown('''
         - Bachelor tesis in  `LDPC codes with linear relationship between word length and minimum distance: upper bound esteem of the frame error rate`.
         ''')

        txt('**High school** , computer science and telecommunications *High shcool Alessando Volta*, Italy',
            '2010 - 2015')
        st.markdown('''
         - As a high school dissertation I brought a model of a remotely controllable home automation house made with Arduino`.
         ''')

    #####################
    if is_section(sections, 'Work experiences'):
        st.markdown('''
         ## Work experiences
         ''')

        txt('**Member**, Contamination LAB, University of Trieste, Italy',
            '2020-2021')
        st.markdown('''
         - The CLab was created with the aim of allowing students to develop their own business idea with the support of teachers and mentors who are experts in the sector. 
         - Thanks to this experience I have had the opportunity not only to realize the knowledge learned in university, but also to learn new techniques that I believe will be useful in my future work, such as, for example, preparing a business plan and a business model to better organize my project and evaluate its potential.
         - The result of this experience and months of work is "Influence", my innovative project that I hope to realize one day. "Influence" represents the perfect synthesis of my experience at Clab, as it reconciles the world of marketing and artificial intelligence. In this sense, my project, through the study of user data, aims to create ever new content that satisfies the changing interests of the public.
         ''')

        txt('**Tutor**, Faculty of Engineering and Architecture, University of Trieste, Italy',
            '2020-2021')
        st.markdown('''
         - Managed the whole area concerning internships and agreements with companies in my department.
         - Facilitated contact between students, companies and universities by following them in the procedure for requesting an internship.
         ''')

        txt('**Help desk First level**, BDF S.p.A, Trieste, Italy',
            'April 2019- August 2019')

        txt('**IT intern**, U_BLOX ITALIA S.p.A., Sgonico, Italy',
            'July 2015- September 2015')

    #####################
    if is_section(sections, 'Skills'):
        st.markdown('''
         ## Skills
         ''')
        txt3('Programming', '`Python`, `Java`, `C` , `C++` , `SQL`, `VBA` , `Linux`')
        txt3('Data processing', ' `pandas`, `numpy`')
        txt3('Data visualization', '`matplotlib`, `Excel`')  # `seaborn`, `plotly`, `altair`, `ggplot2`
        txt3('Machine Learning', '`scikit-learn`')
        txt3('Deep Learning', '`Pycharm` , `Keras`')
        txt3('Web development', ' `HTML`, `CSS` , `WordPress`')

    #####################
    if is_section(sections, 'Courses and certified'):
        st.markdown('''
         ## Courses and certified
         #### Courses at Montanuniversität Leoben 
         - Computational Methods and Tools for Logistics
         - Production Data Analysis and Modelling
         - Decision-Making and Risk Analysis
         - Mechatronic Design Project
         - Fundamentals of Logistics Systems Engineering
    
         #### Courses at the University of Trieste
         - Natural language processing
         - Deep learning
         - Computer vision and pattern recognition 
         - Databases
         - Computer networks 2 and introduction to cybersecurity
         - Foundation of high performance computing course of the HPC master at SISSA
         - Introduction to machine learning and evolutionary robotics
         - Open Data Management and the Cloud in collaboration con INAF
         - Software and operating systems design
    
         #### Extra courses 
         - Business plan
         - Busienss model canvas
         - New product forecasting
         - Storytelling and comunication
         - Leaderschip, team building and social strategies  
         ''')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/giovanni-pinna/')
txt2('Web site', 'https://giovannipinna.net')
txt2('GitHub', 'https://github.com/giovannipinna96')
txt2('YouTube', 'https://www.youtube.com/channel/UCiVRlONi_xbN0Qro6C22y-A')
