"""English (LTR) version of the deck, derived from the Persian source src/deck.html.

Every Persian string is replaced from the tables below; build.py fails if any
replacement no longer matches, so the two versions cannot drift silently.
"""
import html
import re

# Speaker notes, one per slide, in slide order.
NOTES = [
    "In the name of God, the Most Gracious, the Most Merciful.",
    "Right now, 99.99 percent of developers and programmers are shipping a \"feature\". What do I mean by shipping a feature?",
    "I mean that big companies like Gemini, Google, Grok, X, ChatGPT and OpenAI can eat your product for breakfast tomorrow! They can push your product out of the race very quickly. It might even happen immediately! Do you see?",
    "But when you offer a vital, foundational platform, even the big companies come to need it.",
    "Why? Because these companies face a huge number of problems and headaches. Adding a big new project to their portfolio creates a lot of problems and complexity for them. They need to add new features to their products. That is exactly what I am talking about. Big companies should add features, not program a big product from scratch every time. Do you see?",
    "So if you offer them a good product, they are willing to buy it. Even Google! Even OpenAI! Even companies like ASYAD prefer to buy a ready, suitable product.",
    "Especially when your product and platform can be deployed and run on those companies' own servers. Why does this matter? Because they need control. They need security. They must be able to see and oversee what they buy. Do you see?",
    "Before I introduce the product and explain what kind of product I am talking about, let me first show you that we know big companies. We understand companies well. Our team's expertise is in big companies like Meta, OpenAI and Google, and companies with a very large number of users. So we know what these companies need.",
    "And our product... our product gives organizations a triangle. Let me ask a question. In your opinion, what is the main goal of every company? (pause) Well? The answer is profit. The main goal of every company is to earn more profit.",
    "It is simple. But how can you increase your company's profit? That is a very big and important question. You have two ways to increase profit. Way one: reduce costs. Way two: increase added value. Right?",
    "When I say our product gives the organization a triangle, I mean these three: profit, control and insight. This triangle matters to every organization, especially large ones.",
    "We talked about profit. We said there are two ways to increase it. But to use those two ways and earn more profit, you need two wings. Do you see? And these two wings are: wing one, Control; wing two, Insight. When you have control over your company and insight into its situation, you can create more profit.",
    "But here is the real question: how does our platform, our product, give you these two wings to reach that one result? How does it give you control and insight, so that you finally reach more profit? (Move into the product demo here.)",
]

LUNA = {
    "هدف اصلی هر شرکتی چیست؟": "What is the main goal of every company?",
    "پلتفرم ما چگونه این دو بال را به شما می‌دهد؟": "How does our platform give you these two wings?",
}

# (Persian, English) pairs; each Persian string must occur in the source.
TEXT = [
    ('<html lang="fa" dir="rtl">', '<html lang="en" dir="ltr">'),
    ('<title>لونا · از قابلیت تا پلتفرم</title>', '<title>Luna · From Feature to Platform</title>'),
    ('content="ارائهٔ آغازین لونا: گراف دانش سازمان و مثلث سود، کنترل و بینش"', 'content="Luna opening presentation: the organizational knowledge graph and the triangle of profit, control and insight"'),
    ('<a class="langbtn" href="./" lang="en">English</a>', '<a class="langbtn" href="fa.html" lang="fa">فارسی</a>'),
    ('title="یادداشت سخنران (N)">یادداشت</button>', 'title="Speaker notes (N)">Notes</button>'),
    ('title="تمام‌صفحه (F)">تمام‌صفحه</button>', 'title="Fullscreen (F)">Fullscreen</button>'),
    # cover
    ('<div class="bism f" data-f="0">بسم‌الله الرحمن الرحیم</div>', '<div class="bism f" data-f="0">In the name of God</div>'),
    ('گراف دانش سازمان · با صدای لونا', 'The organization’s knowledge graph · voiced by Luna'),
    ('از <span style="color:var(--warn)">«قابلیت»</span> تا <span class="grad">«پلتفرم»</span>', 'From a <span style="color:var(--warn)">feature</span> to a <span class="grad">platform</span>'),
    ('چرا محصولی که غول‌ها نمی‌توانند بخورند، همان محصولی است که می‌خرند.', 'Why the product the giants can’t eat is the product they buy.'),
    ('برای شروع، کلید ← یا Space را بزنید', 'Press → or Space to begin'),
    # 99.99
    ('<div class="kicker">واقعیت امروز</div>', '<div class="kicker">The reality today</div>'),
    ('<h2>از توسعه‌دهندگان، دارند یک <span class="tag">قابلیت</span> می‌سازند.</h2>', '<h2>of developers are shipping a <span class="tag">feature</span>.</h2>'),
    ('منظورم از «ارائهٔ یک قابلیت» چیست؟', 'What do I mean by “shipping a feature”?'),
    # breakfast
    ('<div class="kicker">خطر قابلیت</div>', '<div class="kicker">The feature trap</div>'),
    ('غول‌ها می‌توانند محصول شما را<br><span style="color:var(--warn)">مثل یک صبحانه بخورند.</span>', 'The giants can eat your product<br><span style="color:var(--warn)">for breakfast.</span>'),
    ('aria-label="قابلیت‌های کوچک جذب شرکت‌های بزرگ می‌شوند"', 'aria-label="Small features get absorbed by big companies"'),
    ('text-anchor="middle">گوگل</text>', 'text-anchor="middle">Google</text>'),
    ('text-anchor="middle">جمنای</text>', 'text-anchor="middle">Gemini</text>'),
    ('text-anchor="middle">گروک · X</text>', 'text-anchor="middle">Grok · X</text>'),
    ('>چت‌بات PDF</text>', '>PDF chatbot</text>'),
    ('>خلاصه‌ساز جلسه</text>', '>Meeting summarizer</text>'),
    ('>دستیار ایمیل</text>', '>Email assistant</text>'),
    ('>مترجم هوشمند</text>', '>Smart translator</text>'),
    ('همین فردا. شاید همین امروز. <b style="color:var(--text)">و شما از میدان خارج می‌شوید.</b>', 'Tomorrow. Maybe today. <b style="color:var(--text)">And you are out of the race.</b>'),
    # platform
    ('<div class="kicker">نقطهٔ چرخش</div>', '<div class="kicker">The turning point</div>'),
    ('اما یک <span class="grad">پلتفرم حیاتی</span> را<br>حتی غول‌ها هم لازم دارند.', 'But a <span class="grad">vital platform</span> is something<br>even the giants need.'),
    ('<h3>قابلیت</h3><p>یک گره تنها؛ با یک به‌روزرسانی بلعیده می‌شود.</p>', '<h3>A feature</h3><p>A lone node, swallowed by a single update.</p>'),
    ('font-weight="800">غول</text>', 'font-weight="800">Giant</text>'),
    ('<h3>پلتفرم</h3><p>ستون فقراتی که خود غول‌ها به آن وصل می‌شوند.</p>', '<h3>A platform</h3><p>The backbone the giants themselves plug into.</p>'),
    # build vs add
    ('<div class="kicker">چرا؟</div>', '<div class="kicker">Why?</div>'),
    ('یک پروژهٔ بزرگ و تازه، برای غول‌ها <span style="color:var(--warn)">دردسر</span> است.', 'A big new project is a <span style="color:var(--warn)">headache</span> for the giants.'),
    ('<b>ساختن از صفر</b><ul><li>تیم جدید</li><li>زیرساخت</li><li>داده و یکپارچه‌سازی</li><li>امنیت و انطباق</li><li>نگهداری سال‌ها</li><li>ریسک شکست</li></ul>', '<b>Building from scratch</b><ul><li>New team</li><li>Infrastructure</li><li>Data and integration</li><li>Security and compliance</li><li>Years of maintenance</li><li>Risk of failure</li></ul>'),
    ('<div class="mid f" data-f="1">در برابر</div>', '<div class="mid f" data-f="1">vs</div>'),
    ('<b>افزودن یک قابلیت روی پلتفرم آماده</b><div class="one"><span>محصول آن‌ها</span><i></i><span>پلتفرم شما</span></div>', '<b>Adding a feature on a ready platform</b><div class="one"><span>Their product</span><i></i><span>Your platform</span></div>'),
    ('یک اتصال. سریع، کم‌ریسک، قابل‌کنترل.', 'One connection. Fast, low-risk, controllable.'),
    ('غول‌ها <span class="grad">قابلیت اضافه می‌کنند</span>؛ نه اینکه هر بار از صفر بسازند.', 'Giants <span class="grad">add features</span>. They don’t rebuild from scratch every time.'),
    # they buy
    ('<div class="kicker">نتیجه</div>', '<div class="kicker">The result</div>'),
    ('محصول خوب و آماده را <span class="grad">می‌خرند.</span>', 'A good, ready product? <span class="grad">They buy it.</span>'),
    ('<span>حتی</span> گوگل', '<span>Even</span> Google'),
    ('<span>حتی</span> OpenAI', '<span>Even</span> OpenAI'),
    ('<span>حتی</span> آسیاد', '<span>Even</span> ASYAD'),
    # on-prem
    ('<div class="kicker">به‌خصوص وقتی…</div>', '<div class="kicker">Especially when…</div>'),
    ('پلتفرم روی <span class="grad">سرورهای خودِ آن‌ها</span> اجرا شود.', 'the platform runs on <span class="grad">their own servers</span>.'),
    ('<span class="lbl">سرورهای سازمان شما</span>', '<span class="lbl">Your organization’s servers</span>'),
    ('<b>⌖</b>کنترل', '<b>⌖</b>Control'),
    ('<b>🔒</b>امنیت', '<b>🔒</b>Security'),
    ('<b>👁</b>دید و اشراف', '<b>👁</b>Visibility'),
    # team
    ('<div class="kicker">پیش از محصول</div>', '<div class="kicker">Before the product</div>'),
    ('ما <span class="grad">شرکت‌های بزرگ</span> را می‌شناسیم.', 'We know <span class="grad">big companies</span>.'),
    ('تخصص تیم ما در مقیاس شرکت‌هایی است که با تعداد بسیار زیادی کاربر کار می‌کنند.', 'Our team’s expertise is at the scale of companies serving a vast number of users.'),
    ('<small>مقیاس متا</small>', '<small>Meta scale</small>'),
    ('<small>مقیاس اوپن‌ای‌آی</small>', '<small>OpenAI scale</small>'),
    ('<small>مقیاس گوگل</small>', '<small>Google scale</small>'),
    ('پس می‌دانیم این شرکت‌ها <span class="grad">به چه چیزی نیاز دارند.</span>', 'So we know <span class="grad">what these companies need.</span>'),
    # question
    ('<div class="kicker">لونا می‌پرسد</div>', '<div class="kicker">Luna asks</div>'),
    ('<div class="answer f" data-f="1">سود</div>', '<div class="answer f" data-f="1">Profit</div>'),
    ('هدف اصلی هر شرکتی، سود بیشتر است.', 'The main goal of every company is more profit.'),
    # roads
    ('<div class="kicker">سؤال بزرگ</div>', '<div class="kicker">The big question</div>'),
    ('چگونه سود را افزایش دهیم؟ <span class="grad">دو راه.</span>', 'How do you increase profit? <span class="grad">Two ways.</span>'),
    ('font-size="26" fill="#edc78f">سود</text>', 'font-size="26" fill="#edc78f">Profit</text>'),
    ('fill="#93a1bd">راه اول</text>', 'fill="#93a1bd">Way one</text>'),
    ('font-size="24">کاهش هزینه‌ها</text>', 'font-size="24">Reduce costs</text>'),
    ('fill="#93a1bd">راه دوم</text>', 'fill="#93a1bd">Way two</text>'),
    ('font-size="24">افزایش ارزش افزوده</text>', 'font-size="24">Increase added value</text>'),
    # triangle
    ('<div class="kicker">یک هوش · سه بُعد ارزش</div>', '<div class="kicker">One intelligence · three dimensions of value</div>'),
    ('مثلث <span style="color:var(--profit)">سود</span>، <span style="color:var(--control)">کنترل</span> و <span style="color:var(--insight)">بینش</span>', 'The triangle of <span style="color:var(--profit)">Profit</span>, <span style="color:var(--control)">Control</span> and <span style="color:var(--insight)">Insight</span>'),
    ('color:var(--profit)">سود<small>ارزش بیشتر بسازید</small>', 'color:var(--profit)">Profit<small>Create more value</small>'),
    ('color:var(--control)">کنترل<small>کار را هم‌راستا نگه دارید</small>', 'color:var(--control)">Control<small>Keep work aligned</small>'),
    ('color:var(--insight)">بینش<small>ببینید چه چیز به چه وصل است</small>', 'color:var(--insight)">Insight<small>See what connects</small>'),
    # wings
    ('<div class="kicker">برای پرواز سود</div>', '<div class="kicker">For profit to take off</div>'),
    ('به <span class="grad">دو بال</span> نیاز دارید.', 'you need <span class="grad">two wings</span>.'),
    ('aria-label="کنترل و بینش، دو بال سود"', 'aria-label="Control and insight, the two wings of profit"'),
    ('fill="#91d6c3">کنترل</text>', 'fill="#91d6c3">Control</text>'),
    ('>بال اول · Control</text>', '>Wing one</text>'),
    ('fill="#bea0f1">بینش</text>', 'fill="#bea0f1">Insight</text>'),
    ('>بال دوم · Insight</text>', '>Wing two</text>'),
    ('fill="#edc78f">سود</text>', 'fill="#edc78f">Profit</text>'),
    ('با <b style="color:var(--control)">کنترل</b> بر شرکت و <b style="color:var(--insight)">بینش</b> نسبت به وضعیت آن، سود بیشتری می‌سازید.', 'With <b style="color:var(--control)">control</b> over your company and <b style="color:var(--insight)">insight</b> into its state, you create more profit.'),
    # end
    ('<div class="kicker">سؤال اصلی</div>', '<div class="kicker">The real question</div>'),
    ('چگونه <b style="color:var(--control)">کنترل</b> و <b style="color:var(--insight)">بینش</b> می‌دهد تا به <b style="color:var(--profit)">سود بیشتر</b> برسید؟', 'How does it give you <b style="color:var(--control)">control</b> and <b style="color:var(--insight)">insight</b>, so you reach <b style="color:var(--profit)">more profit</b>?'),
    ('بیایید نشانتان بدهم ←', 'Let me show you →'),
    # chrome and script
    ('<button id="prev" aria-label="قبلی">→</button>', '<button id="prev" aria-label="Previous">←</button>'),
    ('<button id="next" aria-label="بعدی">←</button>', '<button id="next" aria-label="Next">→</button>'),
    ("const fa=n=>String(n).replace(/\\d/g,d=>'۰۱۲۳۴۵۶۷۸۹'[d]);", "const fa=n=>String(n);"),
    ("'یادداشت سخنران · اسلاید '", "'Speaker notes · slide '"),
    # LTR: next is to the right
    ("['ArrowLeft','ArrowDown','PageDown',' ','Enter']", "['ArrowRight','ArrowDown','PageDown',' ','Enter']"),
    ("['ArrowRight','ArrowUp','PageUp','Backspace']", "['ArrowLeft','ArrowUp','PageUp','Backspace']"),
    ("go(e.clientX<innerWidth/2?1:-1)", "go(e.clientX>innerWidth/2?1:-1)"),
    ("go(dx>0?1:-1)", "go(dx<0?1:-1)"),
]


def to_english(src: str) -> str:
    for fa, en in TEXT:
        if fa not in src:
            raise SystemExit(f'en.py: source string not found: {fa[:70]}')
        src = src.replace(fa, en)
    for fa, en in LUNA.items():
        src = src.replace(f'data-luna="{fa}"', f'data-luna="{en}"')
    notes = iter(NOTES)
    src, n = re.subn(r'data-notes="[^"]*"', lambda m: f'data-notes="{html.escape(next(notes))}"', src)
    if n != len(NOTES):
        raise SystemExit(f'en.py: {n} slides but {len(NOTES)} notes')
    left = re.findall(r'[؀-ۿ][^<>"]*', re.sub(r'<(style|script)>.*?</\1>', '', src, flags=re.S))
    left = [t for t in left if t.strip() not in ('فارسی',)]
    if left:
        raise SystemExit('en.py: untranslated text left: ' + ' | '.join(left[:8]))
    return src
