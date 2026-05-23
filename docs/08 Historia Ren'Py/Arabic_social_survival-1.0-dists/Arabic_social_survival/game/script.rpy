# DECLARACIÓN COMPLETA DE IMÁGENES
# BACKGROUNDS
image bg apartment_exterior = "images/apartment_exterior.png"
image bg entrance_hallway = "images/entrance_hallway.png"
image bg family_living_room = "images/family_living_room.png"
image bg dining_table = "images/dining_table.png"
image bg tea_serving_scene = "images/tea_serving_scene.png"
image bg traditional_sitting_room = "images/traditional_sitting_room.png"
image bg family_dinner_atmosphere = "images/family_dinner_atmosphere.png"
image bg night_street_leaving_scene = "images/night_street_leaving_scene.png"

# PERSONAJES VISUALES (SOLO 4 PERMITIDOS)
# Hemos añadido zoom y yalign para que los personajes de alta resolución quepan en pantalla.
image host_friend neutral:
    "images/host_neutral.png"
    zoom 0.4
    yalign 1.0

image host_friend smile:
    "images/host_smile.png"
    zoom 0.4
    yalign 1.0

image mother neutral:
    "images/mother_neutral.png"
    yalign 1.0

image mother smile:
    "images/mother_smile.png"
    yalign 1.0

image abu_tariq neutral:
    "images/father_neutral.png"
    zoom 1.2
    yalign 1.0

image abu_tariq smile:
    "images/father_smile.png"
    zoom 1.2
    yalign 1.0

image younger_sibling neutral:
    "images/sibling_neutral.png"
    zoom 0.4
    yalign 1.0

image younger_sibling smile:
    "images/sibling_smile.png"
    zoom 0.4
    yalign 1.0

# DEFINICIÓN DE PERSONAJES DE TEXTO
define host_friend = Character("Tariq", color="#3498db")
define father = Character("Abu Tariq", color="#e67e22")
define mother = Character("Um Tariq", color="#9b59b6")
define younger_sibling = Character("Amir", color="#f1c40f")
define me = Character("Tú", color="#2ecc71")

# SISTEMA DE PUNTUACIÓN Y VARIABLES OCULTAS CULTURALES
default final_score = 0

default cultural_respect = 0
default hospitality_score = 0
default awkwardness_level = 0
default family_trust = 0
default social_integration = 0

# DEFINICIÓN DE POSICIONES PERSONALIZADAS
transform mid_left:
    xalign 0.25

label start:
    # Introducción inmersiva
    # Música de fondo árabe durante toda la historia
    play music "audio/arabic_hospitality.mp3" fadein 2.0 loop
    scene bg apartment_exterior with fade

    "تبدأ الشمس في الغروب، وتغمر شوارع الحي بضوء ذهبي دافئ.\n(El sol comienza a ponerse, bañando las calles del barrio en una cálida luz dorada.)"
    "العالم العربي معروف بضيافته العميقة والدافئة.\n(El mundo árabe es conocido por su profunda y cálida hospitalidad.)"
    "لكن تحت هذا الدفء توجد قواعد غير مكتوبة. ما يقال غالباً مجرد مجاملة؛ وما يُفعل هو ما يهم حقاً.\n(Pero bajo esa calidez hay reglas no escritas. Lo que se dice a menudo es cortesía; lo que se hace es lo que realmente importa.)"
    "اليوم يوم مهم. بينما تمشي نحو العنوان المدون لديك، تتذكر كيف وصلت إلى هذا الموقف.\n(Hoy es un día importante. Mientras caminas hacia la dirección que tienes anotada, recuerdas cómo llegaste a esta situación.)"

    # Escena 1: La Invitación (Flashback/Recuerdo)
    "البارحة، في الحرم الجامعي...\n(Ayer, en el campus universitario...)"
    
    show host_friend smile at center with dissolve
    host_friend "يا صديقي، يجب أن تزورنا في البيت يوماً ما. عائلتي تريد أن تتعرف عليك."
    host_friend "(Amigo mío, debes visitarnos en casa algún día. Mi familia quiere conocerte.)"
    
    menu:
        "كيف رددت على هذه الدعوة؟\n(¿Cómo respondiste a esta invitación?)"

        "نعم، بالطبع! سآتي هذا الجمعة الساعة 8.\n(¡Sí, claro! Iré este viernes a las 8.)":
            $ final_score -= 1
            show host_friend neutral
            "ابتسم طارق بتوتر قليل. في الثقافة العربية، القبول المباشر وتحديد الموعد فوراً قد يبدو عدوانياً أو متغطرساً بعض الشيء.\n(Tariq sonrió un poco tenso. En la cultura árabe, aceptar de forma tan directa y fijar fecha y hora inmediatamente puede parecer demasiado agresivo o presuntuoso.)"
            host_friend "أه... نعم، ممتاز. سأخبر والدي."
            host_friend "(Eh... sí, excelente. Le diré a mi padre.)"
            
        "يسعدني ذلك، إن شاء الله.\n(Me encantaría, si Dios quiere.)":
            $ final_score += 1
            show host_friend smile
            "ابتسم طارق بانفتاح. استخدام 'إن شاء الله' يظهر فهماً بأن المستقبل ليس بأيدينا، وهي الطريقة الأكثر طبيعية وأدباً للقبول.\n(Tariq sonrió abiertamente. El uso de 'إن شاء الله' demuestra entendimiento de que el futuro no está en nuestras manos, y es la forma más natural y educada de aceptar.)"
            host_friend "إن شاء الله! سيكون شرفاً لنا."
            host_friend "(¡Si Dios quiere! Será un honor para nosotros.)"
            
        "لا أريد أن أكون عبئاً، ربما في يوم آخر.\n(No quiero ser una molestia, mejor otro día.)":
            $ final_score -= 1
            show host_friend neutral
            "رفض دعوة مباشرة هو خطأ ثقافي فادح. الضيافة واجب، ورفضها يكاد يكون إهانة.\n(Rechazar una invitación directa es un grave error cultural. La hospitalidad es un deber, y rechazarla es casi un insulto.)"
            host_friend "لا أبداً! لا توجد إزعاج، البيت بيتك."
            host_friend "(¡No, para nada! No hay molestia, mi casa es tu casa.)"

    hide host_friend with dissolve

    # Escena 2: La Llegada
    show host_friend smile at center with dissolve
    "بالعودة إلى الحاضر... أنت أخيراً أمام مبنى منزله. الوقت المتفق عليه للعشاء هو 20:00.\n(Volviendo al presente... Finalmente estás frente al edificio de su casa. La hora acordada para la cena son las 20:00.)"
    
    menu:
        "في أي وقت تطرق الباب؟\n(¿A qué hora llamas a la puerta?)"

        "أطرق الباب في الساعة 20:00 تماماً.\n(Llamo exactamente a las 20:00 en punto.)":
            $ final_score -= 1
            show host_friend neutral
            "تطرق الباب. تسمع خطوات سريعة وبعض الفوضى بالداخل. الوصول في الوقت المحدد تماماً أحياناً لا يترك هامش المجاملة الذي تستخدمه العائلات للتحضيرات الأخيرة.\n(Llamas a la puerta. Oyes pasos rápidos y algo de caos dentro. Llegar exactamente en punto a veces no da el margen de cortesía que las familias usan para los últimos preparativos.)"
        
        "أطرق الباب في الساعة 20:15 (مع قليل من الهامش).\n(Llamo a las 20:15 (un poco de margen).)":
            $ final_score += 1
            show host_friend smile
            "تطرق الباب في الساعة 20:15. هامش من 10-15 دقيقة هو مثالي. يظهر أنك مسترخٍ وتمنح العائلة وقتاً لتجهيز كل شيء.\n(Llamas a la puerta a las 20:15. Un margen de 10-15 minutos es ideal. Demuestra que eres relajado y das tiempo a la familia para tener todo perfecto.)"
            
        "أطرق الباب في الساعة 21:00.\n(Llamo a las 21:00.)":
            $ final_score -= 1
            show host_friend neutral
            "الوصول متأخراً بساعة دون إشعار هو قلة احترام في أي ثقافة، لكن هنا يؤثر مباشرة على الطعام، الذي ربما يكون قد تم تقديمه بالفعل.\n(Llegar una hora tarde sin avisar es una falta de respeto en cualquier cultura, pero aquí afecta directamente la comida, que probablemente ya esté servida.)"

    # Escena 3: El Ritual de los Zapatos
    scene bg entrance_hallway with fade
    "يُفتح الباب.\n(La puerta se abre.)"
    show host_friend smile at center with dissolve
    host_friend "أهلاً وسهلاً! تفضل، تفضل."
    host_friend "(¡Bienvenido, bienvenido! Adelante, pasa.)"
    "تلاحظ وجود عدة أزواج من الأحذية مصطفة بشكل مثالي بجوار باب المدخل الداخلي.\n(Te das cuenta de que hay varios pares de zapatos perfectamente alineados junto a la puerta de entrada interior.)"
    host_friend "لا تخلع حذائك، البيت بيتك، ادخل."
    host_friend "(No te quites los zapatos, estás en tu casa, entra.)"

    menu:
        "أخبرك طارق صراحة ألا تخلع حذاءك. ماذا تفعل؟\n(Tariq te ha dicho explícitamente que no te quites los zapatos. ¿Qué haces?)"

        "الدخول والحذاء في قدمي.\n(Entrar con los zapatos puestos.)":
            $ final_score -= 1
            show host_friend neutral
            "تدخل بحذائك على السجادة الناصعة. طارق مهذب جداً ليقول شيئاً، لكنك تلاحظ أن نظره يتجه نحو قدميك لجزء من الثانية. ما قاله كان مجرد مجاملة؛ القاعدة الحقيقية هي خلع الحذاء.\n(Entras con tus zapatos sobre la alfombra inmaculada. Tariq es demasiado educado para decir algo, pero notas que su mirada se dirige a tus pies por un microsegundo. Lo que dijo fue cortesía pura; la regla real es quitarse los zapatos.)"
            
        "خلع الحذاء وتركه بجانب الأحذية الأخرى.\n(Quitarte los zapatos y dejarlos junto a los demás.)":
            $ final_score += 1
            show host_friend smile
            "تتجاهل إصراره بأدب وتخلع حذاءك.\n(Ignoras educadamente su insistencia y te quitas los zapatos.)"
            me "شكراً، لكنني أفضل خلعها."
            me "(Gracias, pero prefiero quitármelos.)"
            "يومئ طارق برأسه، ويبدو عليه الارتياح بشكل واضح. لقد فهمت المجاملة غير المباشرة: يجب عليه أن يعرض عليك راحة عدم خلعها، ولكن يجب عليك أن تحترم خلعها.\n(Tariq asiente, visiblemente más aliviado. Has entendido la cortesía indirecta: él debe ofrecerte la comodidad de no quitártelos, pero tú debes tener el respeto de hacerlo.)"

    # Escena 4: El Saludo Familiar (VERSIÓN COMPLETA)
    scene bg family_living_room with fade

    show host_friend neutral at left
    show abu_tariq smile at right

    "تدخل إلى 'المجلس' (غرفة الاستقبال الرئيسية). رجل مسن بوجه ودود ينهض من الأريكة لتحيتك. إنه أبو طارق، الأب.\n(Entras al 'Majlis' (la sala de recepción principal). Un hombre mayor con un rostro amable se levanta del sofá para saludarte. Es Abu Tariq, el padre.)"
    father "مرحباً بك يا بني. شرفتنا."
    father "(Bienvenido, hijo mío. Nos has honrado con tu presencia.)"

    "في آخر الغرفة، تراقب امرأة بابتسامة لطيفة بينما تعد الشاي. إنها أم العائلة.\n(Al fondo de la sala, una mujer observa con una sonrisa suave mientras prepara té. Es la madre de la familia.)"
    show mother smile at center with dissolve
    mother "أهلاً وسهلاً، البيت نور بوجودك."
    mother "(Bienvenido, la casa se ilumina con tu presencia.)"

    "يطل شاب بفضول من الرواق، بتعبير مسترخٍ وودود. إنه الأخ الأصغر.\n(Un joven se asoma curiosamente desde el pasillo, con una expresión relajada y amigable. Es el hermano menor.)"
    show younger_sibling smile at mid_left with dissolve
    younger_sibling "أهلاً! سعيد بلقائك!"
    younger_sibling "(¡Hola! ¡Encantado de conocerte!)"

    menu:
        "كيف تتفاعل أمام العائلة المجتمعة؟\n(¿Cómo reaccionas ante toda la familia reunida?)"

        "التحية البسيطة والبقاء في صمت مهذب.\n(Saludar de forma simple y quedarse en silencio educado.)":
            $ final_score -= 1
            "رد فعلك صحيح ولكنه متحفظ للغاية. أنت لا تخلق تواصلاً مع بقية العائلة.\n(Tu reacción es correcta pero demasiado reservada. No generas conexión con el resto de la familia.)"

        "الرد بتحية رسمية واحترام ثقافي.\n(Responder con saludo formal y respeto cultural.)":
            $ final_score += 1
            me "السلام عليكم ورحمة الله وبركاته"
            me "(Que la paz y las bendiciones de Dios estén con vosotros.)"
            "ترد العائلة بابتسامات دافئة. لقد تركت انطباعاً أولياً ممتازاً بشكل عام.\n(La familia responde con sonrisas cálidas. Has causado una excelente primera impresión global.)"

    hide mother with dissolve
    hide younger_sibling with dissolve

    # Escena 5: El Café Árabe (Gahwa)
    scene bg traditional_sitting_room with fade
    show abu_tariq neutral at right
    "تجلس براحة. فوراً، يظهر طارق وفي يده 'دلة' (صانعة قهوة تقليدية) ذهبية وفناجين صغيرة.\n(Te sientas cómodamente. Inmediatamente, Tariq aparece con una 'Dallah' (cafetera tradicional) dorada y pequeñas tazas (Finjan).)"
    show host_friend smile at left with dissolve
    "يسكب لك القليل من القهوة، ويملأ ثلث الفنجان فقط، ويقدمه لك مباشرة.\n(Te sirve un poco de café, llenando solo un tercio de la taza, y te lo ofrece directamente.)"

    menu:
        "كيف تأخذ الفنجان؟\n(¿Cómo tomas la taza?)"

        "باليد اليسرى، لأنها مريحة لي أكثر.\n(Con la mano izquierda, ya que me queda más cómoda.)":
            $ final_score -= 1
            show host_friend neutral
            "يتردد طارق لثانية قبل ترك الفنجان. في الثقافة العربية (والإسلامية بشكل عام)، تُخصص اليد اليسرى للنظافة الشخصية. استخدامها للأكل أو تلقي الطعام هو من المحرمات القوية.\n(Tariq duda un segundo antes de soltar la taza. En la cultura árabe (y musulmana en general), la mano izquierda se reserva para la higiene personal. Usarla para comer o recibir comida es un tabú fuerte.)"

        "باليد اليمنى، شاكراً.\n(Con la mano derecha, agradeciendo.)":
            $ final_score += 1
            "تأخذ الفنجان بيدك اليمنى. القهوة بنكهة الهيل وهي مُرّة، لكنها لذيذة.\n(Tomas la taza con la mano derecha. El café tiene cardamomo y es amargo, pero delicioso.)"
            
    "تشرب المحتوى. يقترب طارق فوراً ليسكب لك المزيد. القاعدة الذهبية هي أنهم سيستمرون في السكب حتى تطلب منهم التوقف!\n(Bebes el contenido. Tariq inmediatamente se acerca para servirte más. ¡La regla de oro es que servirán hasta que les digas que pares!)"
            
    menu:
        "كيف تشير له أنك لا تريد المزيد من القهوة؟\n(¿Cómo le indicas que no quieres más café?)"
        
        "قول 'يكفي، شكراً!' وتغطية الفنجان باليد.\n(Decir '¡Basta, gracias!' y tapar la taza con la mano.)":
            $ final_score -= 1
            show host_friend neutral
            "خشن قليلاً. يتراجع طارق بالدلة، لكن الطريقة كانت مباشرة وحادة جداً.\n(Un poco brusco. Tariq se retira con la cafetera, pero la forma fue demasiado directa y cortante.)"
        
        "هز الفنجان قليلاً من جانب إلى آخر.\n(Agitar la taza ligeramente de lado a lado.)":
            $ final_score += 1
            "تهز الفنجان برفق بمعصمك، دون أن تنطق بكلمة.\n(Agitas el Finjan levemente con la muñeca, sin decir una palabra.)"
            show host_friend smile
            "يومئ طارق ويبتسم، متراجعاً بالدلة. لقد أتقنت إشارة غير لفظية أساسية في المجلس.\n(Tariq asiente y sonríe, retirando la cafetera. Has dominado una señal no verbal esencial del Majlis.)"

    hide host_friend with dissolve

    # Escena 6: El Banquete y la Insistencia
    scene bg family_dinner_atmosphere with fade
    show abu_tariq smile at right
    "بعد فترة، يُعلن عن العشاء. تنتقلون إلى غرفة أخرى حيث توجد مأدبة ضخمة: أرز الكبسة، لحم خروف طري، سلطات، حمص...\n(Después de un rato, se anuncia la cena. Pasan a otra habitación donde hay un banquete masivo: arroz Kabsa, cordero tierno, ensaladas, hummus...)"
    father "بسم الله، تفضلوا. الأكل قليل، نعتذر عن التقصير."
    father "(En el nombre de Dios, adelante. La comida es poca, pedimos disculpas por nuestras deficiencias.)"
    "تلاحظ جبل الطعام الذي سيكفي لإطعام عشرة أشخاص. القول بأنها 'قليلة' هو مجرد تواضع ثقافي.\n(Observas la montaña de comida que alimentaría a diez personas. Decir que es 'poca' es pura modestia cultural.)"
    "تبدأ في الأكل. كل شيء رائع. عندما تشعر أنك لا تستطيع أكل المزيد، تترك أدوات المائدة.\n(Empiezas a comer. Todo está exquisito. Cuando sientes que ya no puedes más, dejas los cubiertos.)"
    show abu_tariq neutral at right
    father "كل أكثر! أنت لم تأكل شيئاً!"
    father "(¡Come más! ¡No has comido nada!)"

    menu:
        "يأخذ أبو طارق قطعة كبيرة من اللحم الطري ويضعها في طبقك. ماذا تفعل؟\n(Abu Tariq toma un gran trozo de carne tierna y lo pone en tu plato. ¿Qué haces?)"

        "قول 'لا، بجدية، لا أريد المزيد' وترك الطعام في الطبق.\n(Decir 'No, en serio, no quiero más' y dejar la comida en el plato.)":
            $ final_score -= 1
            show abu_tariq neutral at right
            "الرفض المباشر عندما يُقدم لك شخصياً هو وقاحة. ترك الطعام سليماً والذي قُدم كشرف هو أيضاً ازدراء بسيط، حتى لو فهموا أنك شبعت.\n(Rechazar frontalmente cuando te sirven directamente es rudo. Dejar comida intacta que te han servido como honor también es un pequeño desaire, aunque entiendan que estás lleno.)"
            
        "أكل القليل، ثم قول 'الحمد لله'.\n(Comer un poco más, y luego decir 'الحمد لله'.)":
            $ final_score += 1
            show abu_tariq neutral at right
            "تقبل الشرف، وتأكل قليلاً من القطعة التي قدمها لك، ثم تتكئ بلطف، مظهراً رضا حقيقياً.\n(Aceptas el honor, comes un poco del trozo que te ofreció, y luego te reclinas suavemente, mostrando verdadera satisfacción.)"
            me "الحمد لله، شبعت. السفرة دائمة إن شاء الله."
            me "(Alabado sea Dios, estoy lleno. Que vuestra mesa sea siempre abundante, si Dios quiere.)"
            show abu_tariq smile at right
            "يبتسم أبو طارق باتساع، وهو مسرور. لقد شاركت في طقس 'الإصرار والقبول'، وختمت بعبارة الشكر المثالية.\n(Abu Tariq sonríe ampliamente, complacido. Has participado en el ritual de 'insistir y aceptar', y has cerrado con la frase de agradecimiento perfecta.)"

    # Escena 7: Conversación y Preguntas Personales
    scene bg traditional_sitting_room with fade
    show abu_tariq neutral at right
    show host_friend smile at left
    "بالعودة إلى غرفة المعيشة، يقدم طارق الشاي الحلو بالنعناع.\n(De vuelta en la sala de estar, Tariq sirve té dulce de menta.)"
    father "أخبرني يا بني، كم راتبك في وظيفتك؟ وهل أنت متزوج؟"
    father "(Dime hijo mío, ¿cuánto es tu salario en tu trabajo? ¿Y estás casado?)"
    "في العديد من الثقافات الغربية، قد تكون هذه الأسئلة تطفلية وغير مهذبة للغاية.\n(En muchas culturas occidentales, estas preguntas serían increíblemente invasivas y descorteses.)"

    menu:
        "كيف تتفاعل مع هذه الأسئلة الشخصية جداً؟\n(¿Cómo reaccionas ante estas preguntas tan personales?)"

        "هذه أسئلة خاصة، أفضل عدم الإجابة.\n(Esas son preguntas privadas, prefiero no contestar.)":
            $ final_score -= 1
            show abu_tariq neutral at right
            show host_friend neutral
            "يبرد الجو على الفور. بالنسبة لهم، طرح هذا السؤال هو علامة على أنهم يعتبرونك قريباً ويهتمون برفاهيتك. إجابتك الدفاعية رفعت جداراً من الجليد.\n(El ambiente se enfría instantáneamente. Para ellos, preguntar esto es una señal de que te consideran cercano y se preocupan por tu bienestar. Tu respuesta defensiva ha levantado un muro de hielo.)"
            
        "الإجابة بشكل عام وبأدب.\n(Responder de forma general y amable.)":
            $ final_score += 1
            show abu_tariq neutral at right
            show host_friend smile
            "تدرك بسرعة أن هذه طريقتهم في إظهار الاهتمام الصادق والرعاية الأبوية.\n(Entiendes rápidamente que es su forma de mostrar interés genuino y preocupación paterna.)"
            me "الحمد لله، الراتب يكفي وأنا مرتاح. أما الزواج، فكل شيء قسمة ونصيب."
            me "(Alabado sea Dios, el salario es suficiente y estoy a gusto. En cuanto al matrimonio, todo es destino y la voluntad de Dios.)"
            show abu_tariq smile at right
            show host_friend smile
            "يومئ أبو طارق بشدة، وهو راضٍ جداً عن نضجك وحكمتك وتواضعك.\n(Abu Tariq asiente vigorosamente, muy satisfecho con tu madurez, discreción y humildad.)"

    # Escena 8: La Falsa Despedida
    scene bg tea_serving_scene with fade
    show abu_tariq smile at right
    show host_friend neutral at left
    "لقد أمضيت 3 ساعات ونصف في المنزل. طار الوقت، لكن حان وقت الذهاب.\n(Llevas ya 3 horas y media en la casa. El tiempo ha volado, pero es hora de irse.)"
    me "يجب أن أذهب الآن، تأخر الوقت."
    me "(Debo irme ya, se ha hecho tarde.)"
    show abu_tariq neutral at right
    father "مستحيل! الوقت مبكر جداً! يجب أن تأكل بعض الفواكه."
    father "(¡Imposible! ¡Es muy temprano! Debes comer algo de fruta.)"

    menu:
        "يمنع الأب خروجك دبلوماسياً بعرض المزيد من الطعام. ماذا تفعل؟\n(El padre bloquea tu salida diplomáticamente ofreciendo más comida. ¿Qué haces?)"

        "قول 'بجدية، يجب أن أذهب' والمشي نحو الباب.\n(Decir 'De verdad, tengo que irme' y caminar hacia la puerta.)":
            $ final_score -= 1
            show abu_tariq neutral at right
            show host_friend neutral
            "مفاجئ جداً. أنت تودعهم، لكنك قطعت الطقس الدقيق للوداع، والذي يتطلب في العالم العربي وقتاً وإصراراً ومراحل متعددة.\n(Demasiado abrupto. Te despides, pero has cortado el delicado ritual de la despedida, que en el mundo árabe requiere tiempo, insistencia y varias etapas.)"
            
        "الجلوس مرة أخرى وقبول القليل من الفاكهة.\n(Sentarte de nuevo y aceptar un poco de fruta.)":
            $ final_score += 1
            show abu_tariq smile at right
            show host_friend smile
            "تجلس مرة أخرى مبتسماً وتأخذ تفاحة. أنت تفهم أن المحاولة الأولى للمغادرة ليست نهائية أبداً. تبقى 20 دقيقة أخرى تتحدث باسترخاء.\n(Te sientas de nuevo sonriendo y tomas una manzana. Entiendes que el primer intento de irse nunca es el definitivo. Te quedas 20 minutos más conversando relajadamente.)"

    # Escena 9: La Despedida Real
    scene bg entrance_hallway with fade
    show abu_tariq smile at right
    show host_friend smile at left
    "الآن، بعد الحلوى، حان وقت المغادرة الفعلي. يمشي الجميع معك إلى الباب.\n(Ahora sí, tras el postre, es el momento real de partir. Todos caminan contigo hasta la puerta.)"
    father "شرفتنا. لا تقطعنا، اعتبر هذا البيت بيتك."
    father "(Nos has honrado. No dejes de visitarnos, considera esta casa tu casa.)"

    menu:
        "كيف ترد على هذا العرض الرائع من الضيافة؟\n(¿Cómo respondes a esta gran muestra de hospitalidad?)"

        "شكراً على كل شيء، مع السلامة.\n(Gracias por todo, adiós.)":
            $ final_score -= 1
            show abu_tariq neutral at right
            show host_friend neutral
            "جاف قليلاً وعملي لختام ليلة مليئة بالكرم والضيافة.\n(Un poco seco y transaccional para cerrar una noche de tanta generosidad y hospitalidad.)"
            
        "الله يسلمك. البيت عامر بأهله، شكراً على حسن الضيافة.\n(Que Dios te proteja. Que esta casa siempre esté próspera con su gente, gracias por su gran hospitalidad.)":
            $ final_score += 1
            show abu_tariq smile at right
            show host_friend smile
            me "الله يسلمك. البيت عامر بأهله، شكراً على حسن الضيافة."
            me "(Que Dios te proteja. Que esta casa siempre esté próspera con su gente, gracias por su gran hospitalidad.)"
            "يضع طارق وأبوه أيديهما اليمنى على قلبيهما، ويومئان بتقدير عميق عند وداعك.\n(Tariq y su padre ponen la mano derecha sobre el corazón, asintiendo con profundo aprecio al despedirse de ti.)"

    # Escena 10: Epílogo y Finales (Ir a evaluación)
    jump ending_check


label ending_check:
    if final_score <= 3:
        jump bad_ending
    elif final_score <= 7:
        jump neutral_ending
    else:
        jump best_ending


label bad_ending:
    scene bg night_street_leaving_scene
    show host_friend neutral at center with dissolve
    "تنتهي الزيارة بشعور غير مريح.\n(La visita termina con una sensación incómoda.)"
    "تودعك العائلة بأدب، ولكن بمسافة.\n(La familia te despide con educación, pero con distancia.)"
    "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\nنتيجتك النهائية | Tu puntuación final\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    "🏆 النقاط المكتسبة: [final_score] / 10\n(Puntos obtenidos: [final_score] / 10)\n\nلا تستسلم، الثقافة تُتعلَّم بالتجربة!\n(¡No te rindas, la cultura se aprende con la experiencia!)"
    stop music fadeout 3.0
    return

label neutral_ending:
    scene bg family_living_room
    show host_friend smile at left with dissolve
    show abu_tariq neutral at right with dissolve
    "تمضي الأمسية بشكل طبيعي.\n(La velada transcurre con normalidad.)"
    "لقد أظهرت الاحترام، ولكن دون أن تبرز كثيراً.\n(Has mostrado respeto, pero sin destacar demasiado.)"
    "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\nنتيجتك النهائية | Tu puntuación final\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    "🏆 النقاط المكتسبة: [final_score] / 10\n(Puntos obtenidos: [final_score] / 10)\n\nليس سيئاً! يمكنك تحقيق نتيجة أفضل.\n(¡Nada mal! Puedes conseguir un mejor resultado.)"
    stop music fadeout 3.0
    return

label best_ending:
    scene bg family_dinner_atmosphere
    show host_friend smile at left with dissolve
    show abu_tariq smile at right with dissolve
    "تتدفق الليلة بطبيعية وتناغم.\n(La noche fluye con naturalidad y armonía.)"
    "لقد حققت تواصلاً حقيقياً مع العائلة.\n(Has logrado una conexión genuina con la familia.)"
    "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\nنتيجتك النهائية | Tu puntuación final\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    "🏆 النقاط المكتسبة: [final_score] / 10\n(Puntos obtenidos: [final_score] / 10)\n\nممتاز! أتقنت آداب الضيافة العربية!\n(¡Excelente! ¡Has dominado las normas de hospitalidad árabe!)"
    stop music fadeout 3.0
    return
