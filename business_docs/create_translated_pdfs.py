from pathlib import Path
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import inch

OUTPUT_DIR = Path('business_docs_en')
OUTPUT_DIR.mkdir(exist_ok=True)

pmf_mfp_text = '''⭐ 4 Fits

PMF (product-market-fit)

Everyone knows you need to find PMF (product-market-fit).
Most likely, even people who use the term do not explain it correctly.
They will say something like “it is when a project finds its market.”

Let's understand why PMF is great, but not mandatory. And let's also
review the remaining “fits” so you can show off your knowledge.
And of course, how to apply it.

There will be a lot of text, but understanding it is very important for
your marketing to turn from “we will pour traffic” or “we will have
organic traffic” into something meaningful.

Part 1: Why product-market fit is not enough

It is not just about a great product

The standard answer to almost any question in startups is “build a
great product.” But building a great product is only part of the puzzle.
There are great products that never reach $100 million+. There are also
terrible products, by most people's definitions, that reach far more than
$100 million. (For example, Workday, which at the time of writing is
worth $20 billion.)

“Build a great product” cannot be the answer. It is a starting point, but
not the answer.

The problem with that answer is that it leads to the product death cycle.
Here are its phases:

1. Adding new features: The team adds new features.
2. Launch: The features launch with some press coverage.
3. Spike: A short-term growth spike occurs.
4. Growth levels off: After a few weeks, growth levels off.
5. Adding new features (repeat): The team goes back to where it started.

The growth curve looks something like this, and it is not the growth curve
we are looking for.

It is not only about product-market fit

The second standard answer is Market Product Fit. Although it is an
important component, it is far from the answer. The problem is that we
have taken this mantra to the extreme and developed tunnel vision.

Statements like “Market Product Fit is the only thing that matters” have
become normal. But that is not the only thing that matters.

There are many companies that have all the signals of product-market
fit but still struggle to grow. The key point: Market Product Fit is not the
only thing that matters.

It is definitely not growth hacking

Another common answer is “growth hacking.” This concept assumes there
is some trick, secret, or hack that will unlock growth. The problem with
such hacks is that they are not durable and are never sustainable.

Before tactics, you need a growth process. But before the growth
process, you need a strategy. This structure is all about how you build
your strategy.

What is the difference?

What is the difference between companies worth $100 million+ and those
that struggle? The difference is that the first group managed to assemble
four pieces of the puzzle. There are four main fits: Market Product Fit,
Product Channel Fit, Channel Model Fit, and Model Market Fit.

There are three extremely important points:

1. You need to find four fits to grow to a $100 million+ business in a
reasonable time.
2. Each of these fits affects the others, so you cannot think of them in
isolation.
3. Fits always evolve, change, or break. When that happens, you cannot
just change one element; you need to review and potentially change them
all.

Part 2: The path to a $100 million business does not start with the
product

Instead of repeating many excellent posts that explain Market Product
Fit, we will focus on five elements that are most often misunderstood:

1. The wrong way to search for Market Product Fit.
2. Why we must think of it as “Market Product Fit” (market fitting the
product).
3. How to define market and product hypotheses.
4. What the search looks like in reality, not theory.
5. Qualitative, quantitative, and intuitive signals of Market Product Fit.

A common mistake is to have a solution (product) that is looking for a
problem and a market. In other words, putting the cart before the horse.

Instead, we should have focused on the problem and market first, and then
looked for the solution. This common mistake is why the term “Market
Product Fit” (market fit to product) is preferable to “Product Market Fit”
(product fit to market).

The reason is that the real problem is what your market and audience
experience, not what lives in your product. Language matters. The way we
phrase things influences how we think about them.

Finding market-product fit the right way

Instead of focusing on the product first, concentrate on defining the
market.

There are four key market elements to consider:

1. Category. What category does the customer place you in?
2. Who. Who is the target audience in that category?
3. Problems. What category-related problems does your target audience
have?
4. Motivations. What motivates these problems?

Here is how these four elements roughly looked for HubSpot’s division:

Although most companies understand “category” and “who,” defining the
problems and motivations behind them is far more important.

Based on that definition of problem and market, the team can start
to think about the product (solution). That brings us to the next group
of elements — product hypotheses. Four main elements:

1. Core value proposition. What is the product’s core value proposition?
How does it relate to the main problem?
2. Hook. How can the core value proposition be expressed in the simplest
terms?
3. Time to value. How quickly can the target audience experience value?
4. Stickiness. How and why will customers stay? What are the natural
retention mechanics of the product?

These hypotheses are extremely important to articulate. They inform and
deeply influence the other structure components, such as Channel and
Model.

The reality of searching for market-product fit

In practice, the search for Market Product Fit is never a straight line.
Instead, it occurs over several iterative cycles. You start with the market,
build an initial version of the product, see who actually gets value, then
redefine the market and redefine the product.

Often you discover many more target personas beyond your initial
hypothesis.

Market-product fit is not binary

The iterative Market Product Fit cycle brings us to another key point:

Market Product Fit is not binary. It is also not a single point in time.

It is better to think of Market Product Fit as a spectrum from weak to
strong.

When you present Market Product Fit as a binary concept, you imply that
your market and product components do not change. We know in
practice that this is far from true.

There are two main ways the market changes for a startup.

1. MARKET DEFINITION EXPANDS. Most startups start with a very niche
market and expand their definition outward to larger markets. To expand
into those layers, the product typically has to change to maintain the
strength of Market Product Fit.

2. THE MARKET EVOLVES. At the same time, markets do not stand still.
That means markets where you have strong Market Product Fit will evolve
over time. For example, the shift from web to mobile.

Signals of Market Product Fit

If Market Product Fit is not binary, how do you know whether you have it?
Almost everything requires combining qualitative measures with
quantitative measures and your own intuition.

1. QUALITATIVE. The usual starting point is qualitative indicators. To get
qualitative insight, use loyalty surveys. If you are truly solving the
customer’s problem, they should be willing to recommend your product to
a friend.

2. QUANTITATIVE. There are two quantitative measures: retention curves
and direct traffic.

Flat retention curves indicate Market Product Fit. For 80% of products,
flat retention curves are what you are looking for.

The second quantitative signal is direct traffic. Direct traffic is usually
a result of word-of-mouth.

Together, these mean that a product with Market Product Fit will grow
naturally without additional effort.

3. INTUITION. Intuition is an internal gut feel. It is hard to intuit whether
you have Market Product Fit if you have not been in different situations.
The point is that when you have strong Market Product Fit, it feels like
the market pulls you forward rather than you pushing the market.

Key takeaways

- Start with the market (problem), then the product (solution). Not the
other way around.
- Define your market hypothesis (Category, Who, Problems,
Motivations).
- Define your product hypothesis (Core value proposition, Hook, Time
to value, Stickiness).
- Think of Market Product Fit as a cycle.
- Understand that Market Product Fit is not binary. It is a spectrum.
- To know whether you have Market Product Fit, combine qualitative,
quantitative, and intuitive indicators.

Part 3: Product-channel fit will make or break your growth strategy

A common belief is: “We are focused on Market Product Fit now. Once we
get it, we will test a bunch of different channels.”

There are two serious problems with that statement.

1. Products are built to fit channels, not the other way around.

The first problem with that statement is that you think about product
and channel separately, in isolation. But if you think that way, you will
end up trying to fit a square peg into a round hole. Why? Because...

Products are built to fit channels. Channels do not adapt to products.

The reason is that you do not define the rules of the channel. The
channel defines the rules of the channel.

- Facebook defines what content appears in people’s feeds.
- Google defines what content appears in the top ten search results.
- Email clients define what counts as spam.

You control your product; you do not control the channel. Therefore,
you need to change what is within your control to fit what you do not
control.

What are the common product attributes that match different channel
categories?

- Virality needs:
  - Fast time to value. Viral loops must be short.
  - A broad value proposition.
  - A network that makes the product better.

- Paid marketing needs:
  - Fast time to value. Users have less patience.
  - A medium-to-broad value proposition.

- Transactional models need:
  - A product that extracts value to fund marketing.

- UGC SEO needs:
  - User-generated content. The product should allow users to create
    millions of pieces of unique content.
  - Motivations for participation.

2. The power law of distribution

The second problem with “we will test a bunch of different channels” is
this: in his book Zero to One, Peter Thiel explained why this is wrong:
“Most companies do not get even one working distribution channel. If
you get at least one channel to work, you have a great business...
Distribution obeys a power law.”

In other words, at any given time, a company with Product Channel Fit
will get 70%+ of its growth from one channel.

If you look at most $100 million+ companies:

- UGC SEO: TripAdvisor, Yelp, Glassdoor — all got 70% of their
growth from here.
- Virality: WhatsApp, Evernote, Dropbox — all got 70%+ of their
growth from here.
- Paid marketing: Supercell, Squarespace, Blue Apron — all got 70%+
of their growth from here.

Product Channel Fit is when the attributes of your product are shaped
to match a specific distribution channel. As a result, you cannot think
about Product and Channel in isolation.

This has several direct consequences:

1. You should not use a “shotgun approach” to channel testing. It is
better to prioritize and focus on one or two channels at a time.
2. You should not try to diversify channels for the sake of
diversification.
3. Product and growth teams should not work in isolation from each
other.

Product Channel Fit is your blessing and your curse

Your strength is also your greatest weakness. Product Channel Fit can
build your company, and it can also kill it.

The reason is that Product Channel Fit (like all other fits) always
evolves and can break.

1. New channels appear. From time to time, a new major channel
emerges in the ecosystem. When this happens:

- Companies from the old channel try to copy-and-paste their product
  into the new channel.
- Because of Product Channel Fit, that does not work and it leaves the
door open for new companies.

There is no brighter example than the gaming industry. In the early
2000s, web portals were the main channel (for example, PopCap).
Then in 2007, social networks became the new channel (for example,
Zynga). Old companies tried to copy-and-paste their games, and it
did not work. Then mobile devices appeared. Zynga tried to
copy-and-paste its games, and it did not work. The door opened for
companies like Supercell.

This is worth repeating: products must be adapted to the channel.
The channel does not adapt to the product.

2. Old channels die. At the end of 2011, Pinterest’s growth began to
soar. One reason was that they achieved Product Channel Fit with
Facebook (viral sharing via API). But around late 2012, Facebook
began closing those APIs.

This is an example of having Product Channel Fit but it breaking.
Pinterest was one of the few companies that successfully transitioned.
They moved to UGC SEO, which has driven their growth since.
Part of that transition was Pinterest shifting its product focus from
social to personal utility. Again, you must adapt the product to the
channel.

Part 4: Get out of the danger zone with Channel Model Fit

Channel Model Fit is simple: channels are determined by your model.

First, what is meant by “model”? The two most important elements of
your model are:

1. How you charge — for example, free (ad-supported), freemium,
transactional, trial, etc.
2. Average revenue per user — how much money you get from a
customer each year.

Why average annual revenue, not lifetime value? Because most
startups need payback in under one year. If it is much longer, you will
need a lot more money to finance growth.

The ARPU ↔ CAC spectrum

Every business lives on the spectrum between ARPU (average revenue
per user) and CAC (customer acquisition cost).

- On the left end (low ARPU) are businesses forced to use low-CAC
  channels. Most consumer ad-based businesses (Facebook, Yelp)
  live here. They use virality and UGC SEO.
- One step to the right are businesses with slightly higher ARPU
  (for example, subscription commerce like Dollar Shave Club). Because
they have higher ARPU, they can use channels with higher CAC, such
as paid marketing.
- Further right are businesses with higher ARPU (typically B2B mid-
  market), such as HubSpot. They can use high-CAC channels like
  content marketing or inside sales.
- At the far right are businesses with very high ARPU (6-7 figures).
  They use very high CAC channels such as enterprise and outbound
  sales (for example, Palantir).

The ARPU-CAC danger zone

The middle of the spectrum is empty. This is the Danger Zone.

Companies that land in this zone have a much higher failure rate
because they lack Channel Model Fit. There are two reasons:

1. Too much friction for low-CAC channels. Low-CAC channels
require low-friction products. Companies in the danger zone have
ARPU that is too high and creates too much friction (for example, a
$500 price) for an impulse purchase via simple advertising.

2. ARPU does not support higher-CAC channels. Companies in the
danger zone also have ARPU that is too low to support higher-CAC
channels (like content marketing or a sales team). These companies
end up with terrible unit economics.

Can companies exist in the danger zone?

The danger zone does not mean a business cannot exist there. But your
acquisition strategy ultimately becomes a patchwork of many small
channels instead of owning one. Stitching together many small
channels is much harder.

Takeaways from Channel Model Fit

There are two main takeaways:

1. Do not consider model and channel in isolation. If your channel is
defined by your model, but your product is built to fit the channel —
you see where I’m going? This is why you cannot treat these fits
separately.

Part 5: The Model Market Fit threshold and what it means for your
growth strategy

Model Market Fit

Model Market Fit is the concept that your market (and the number of
customers in that market) impacts your model.

This concept can be broken into five main business types:

- Elephants — 1,000 customers paying $100,000+ per year.
  (Enterprise clients.)
- Moose — 10,000 customers paying $10,000+ per year. (Mid-market.)
- Rabbits — 100,000 customers paying $1,000 per year. (Small business
  or high-end consumer purchases.)
- Mice — 1,000,000 customers paying $100 per year. (Power users or
  subscription commerce.)
- Flies — 10,000,000 customers paying $10 per year (usually ad-
  supported).

We can draw a line through this relationship. This is called the Model
Market Fit Threshold.

If your business sits above that threshold, you have Model Market Fit.
If you are below the threshold, you do not.

How do you know if you have Model Market Fit?

Your hypothesis for Model Market Fit revolves around simple math:

ARPU x total customers in the market x % you believe you can capture
>= $100 million

This may seem simple, but many teams do not do it. Each variable in this
equation has assumptions:

Total customers in the market. First, define your target market.
Research how many target customers fit those criteria. If this number
is too small, you can expand the criteria, but then you need to go back
to Market Product Fit.

ARPU (average revenue per user). After defining the market, research
willingness to pay. If it is too low, consider increasing prices. But if
you raise prices, you must ensure Channel Model Fit still holds.

% you can capture. This variable is probably the hardest to forecast.
It is easy to overestimate the percentage you think you can capture.

What should you do with this?

Describe how you see Market Product Fit, Product Channel Fit,
Channel Model Fit, and Model Market Fit.

Answer the following questions:

1. What is the #1 problem you solve?
2. Why do customers urgently need a solution?
3. Why will they stay for the long term?
4. What one channel can currently deliver 70%+ of your growth?
5. Why is your product perfect for that channel?
6. Is your model (ARPU) viable at your channel cost (CAC)?
7. Where is your weakest link?

- Describe which of the 4 fits is currently “broken” or missing.
- Example: “We have Market-Product Fit (Step 1) and Model-Market Fit
  (Step 4), but we are stuck in the ‘Danger Zone’ (Step 3) because our
  Channel-Model Fit is broken.”

8. Change hypothesis:

- What one change in one element (Market, Product, Channel, or
  Model) should you test first?
- Change the Market (Who/Problem)
- Change the Product (Value/Hook)
- Change the Channel (Find a new dominant one)
- Change the Model (ARPU/Pricing)

9. What one, riskiest hypothesis from your audit must prove true for
your entire growth machine (all 4 fits) to work at full strength?
'''

pmf_while_ai_text = '''4 Fits in the AI Era

Ask AI

Chapters
Focus Mode

⭐ How artificial intelligence changes growth: product, market,
channel, model

Again, to build successful products you must consider four principles:

- Product-market fit
- Product-channel fit
- Channel-model fit
- Business-model-market fit

Product

Artificial intelligence expands both the problem space and the
solution space. You can now tackle problems that were too difficult
before, and find new ways to solve old problems that previously could
not be solved.

The capabilities of large language models roughly double every seven
months. This is not gradual change; it is exponential growth. That means
the set of available tasks and solutions is expanding very quickly. An
agent can fully complete a task that used to take a client 8, 40, 80 hours
or more. These are exactly the kinds of changes we have already
encountered and will continue to face.

As new tasks arrive, you will need to look for new markets and new
channels. More solutions alone do not guarantee better market fit.

Market

Artificial intelligence expands some markets and, conversely,
contracts others. Canva has always positioned itself as a design service
for everyone, and its potential audience is now growing rapidly. When a
user can simply describe a desired outcome instead of manually moving
elements and picking colors, this becomes real.

The same is happening with AI tools for building apps, such as Lovable
and Bolt: they have turned a niche no-code market into something far
more mainstream.

But there is a flip side. Chegg, a study help service, lost its previous
product-market fit in just a few months. Customer support tools were
based on live interaction, and they began selling to companies that
now need fewer such employees. Today AI strengthens the support
function and, in some cases, can almost completely replace human
involvement.

How AI changes customer expectations:

Old expectations

New expectations

- A place where I can create something
- Do the work for me
- Made specifically for me
- One size fits all, and I customize it for myself
- I am willing to wait
- I do routine work myself
- I want to get it right now
- Routine work is done for me
- I will pay for every seat
- I will pay for the result
- The tool sees what I do
- The tool has no context
- I will master this interface
- The interface adapts to me

Channel

Old distribution channels are getting worse: SEO is declining, social
networks are closed off, and ad platforms are becoming more expensive.
This is due to AI and the typical platform cycle: first they open for
growth, then they restrict access in order to monetize. Right now most
strong channels are already in the “closing” stage.

The distribution opportunity is already taking shape around ChatGPT and
AI search, but for now it is more of a rapidly growing discovery and
recommendation channel than a true mass source of traffic for all types
of businesses.

Model

AI is changing product economics and pricing. Supporting users is
becoming more expensive because running the models costs real money.
The more complex the scenarios, the higher the token consumption,
and users still want the newest, most expensive models. At the same
time, willingness to pay for AI products is still not fully clear: the
initial novelty effect fades, and product value will need to be proven
again.

Customer demand for AI is incredibly high, but that does not
automatically guarantee profit or business sustainability.

What happens when artificial intelligence changes everything at once?

How product-market fit changes

Companies can almost instantly find and lose product-market fit. It is
important to understand that this state is temporary. In the past, markets
and technologies also changed, but slowly enough that companies had
time to adapt.

For example, during the transition to mobile devices, new capabilities
appeared gradually: technologies evolved annually, the developer
ecosystem formed over time, and mass adoption of smartphones and
fast internet took years. So the gap between new capabilities and
changing customer expectations was several years, and business had time
to restructure.

But with artificial intelligence, something different is happening. The
time between these stages is much shorter.

- New AI capabilities appear monthly, if not weekly.
- A broad developer ecosystem is already formed around this new
  technology, and it continues to grow.
- This technology spreads among hundreds of millions of people quickly,
  cheaply, and freely.

As a result, we see that the product-market fit threshold does not simply
accelerate; it shifts. And when it shifts, a company can lose product-
market fit overnight.

Example: Chegg is a good illustration. Chegg’s main subscription offered
students help with homework. In January 2024, its value was estimated at
$1.2 billion. By October 2024 (nine months later) it was worth $150
million. In nine months, its value fell by 90%, and its subscriber base
shrank by half a million. If the company was nearly break-even in 2023,
then in the third quarter of 2024 it lost $600 million.

Chegg’s attempt to bring a new AI-based product to market failed. It
launched its first AI-driven features 26 months after ChatGPT. In the past,
that could have been considered a fast enough response — but not in the
age of artificial intelligence.

How product-channel fit changes

The principle of product-channel fit says that products adapt to channels.
All successful products are built on top of another channel. TikTok used
Facebook ads, Booking used Google ads, and HubSpot used Google
search optimization.

Channels do not adapt to your product. This is because you do not
control the channels where your audience lives. You play by their rules.

What happens if a channel stops meeting market requirements?

Imagine a scenario where a major platform like Google suddenly stops
meeting market requirements. The consequences would be catastrophic
and widespread. Companies like TripAdvisor and Pinterest, which rely
heavily on search traffic, would face serious problems. This would affect
thousands of smaller companies that depend on those intermediary
platforms. Companies need to watch their distribution channels closely
and prepare for disruption.

What if a new channel appears?

When Facebook emerged in 2007, people did not stop visiting web game
portals like Webclip and Yahoo Games. But suddenly there was a new
place where people spent a lot of time and formed new habits. Web
game companies tried to move their games into Facebook and failed.
The games were not designed for how people behaved in that social
context (playing with friends rather than alone).

The gap with ChatGPT is happening right now.

In many categories, people now start searches with ChatGPT instead of
traditional search engines or specialized sites. This is a fundamental
shift in user behavior and starting points. The consequences differ greatly
by industry. Companies selling products that require careful selection,
such as travel packages or cars, face immediate challenges. Before
reaching traditional booking sites or dealer websites, users conduct
thorough research with ChatGPT. These companies need to understand
how to adapt their products to work with AI, or they risk losing clients to
competitors.

You are vulnerable even when your channels seem stable.

If your audience starts spending more time and attention on new
channels, you need to figure out what those channels are as soon as
possible. Otherwise you risk losing to a new player who masters those
channels first.

When choosing Channel Model Fit, the channels that work for you are
determined by your monetization model (how you charge, when you
charge, what you charge for, and how much you charge).

Some companies with low ARPU must use low-CAC channels. Others
with high ARPU can use high-CAC channels.

Channel Model Fit can break for several reasons:

1. AI raises the cost of using the product, causing the old monetization
   model — especially for free and low-cost products — to stop working.
2. At the same time, familiar acquisition channels such as SEO may
   weaken, forcing companies to shift to more expensive channels,
   which requires rethinking pricing and product economics.
3. AI also changes user behavior: people begin to expect a fast, easy,
   and nearly seamless purchase path, causing traditional funnels and
   channels to lose effectiveness quickly.

When that balance breaks, a company risks falling into the “danger
zone”:

1. The product is too expensive and too complex for cheap channels,
   but not lucrative enough for expensive ones. This can lead to slower
growth, churn, higher CAC, worse unit economics, and forced changes
   in pricing and product mix.
2. In those conditions, companies that build flexibility into their
   monetization early and can quickly rewire channels when the market
   changes win.

If the AI wave turns your existing segment into a mass commodity, you
may need to move toward more expensive customers and start serving
enterprise buyers, which requires building (and funding) a higher-touch
sales organization. Or you may need to shift toward cheaper customers
— lowering ARPU and relying on low-touch channels. Either way, you
will likely need a major change in approach, which can be risky,
costly, and time-consuming.

How model-market fit changes

Some markets are experiencing a real boom. Companies like Cursor and
Windsurf are entering much larger markets. AI writes code, which means
many more people can build products. Lovable, Bolt, Replit, and v0 are
bringing this technology to a new level and conquering entirely new
markets. Building applications without writing code opens almost
limitless possibilities.

Replit’s revenue has grown 50x over the past 12 months; the company
has 40 million users and 175,000 paying customers, according to Sacra.
The company grew rapidly thanks to product momentum and huge
interest in coding. Since then it has focused on team and enterprise
adoption, aiming to become a B2B utility for product and design teams.

In this case, the spark is a large market, but only 0.44% of Replit users
are willing to pay. Thus, even though...'''

# Complete the second document translation using the remaining extracted source text.
pmf_while_ai_text += '''...only 0.44% of the market is paying. Therefore, despite the huge
opportunity, the business still needs to find a viable monetization path.

That freemium plans can generate huge amounts of free usage does not
mean they are automatically successful. (1) That free usage can be
expensive, and (2) it is not always a clear signal that users will pay for
additional features.

Carta reports that more than 1,700 startups shut down in 2023 and 2024,
which is a significant increase compared with previous years. Good ideas,
excellent products, and even strong user interest ≠ long-term success.

Change in buyer persona

AI creates new buyer archetypes with different authority, timelines, and
success metrics. The traditional IT buyer focuses on features and
integration. The AI buyer often comes from operations and evaluates
a solution based on labor savings and process automation. Approval
processes, budget sources, and implementation timelines are completely
different than when buying traditional software.

Many of us are so used to switching from one free or freemium AI tool
to another that it is hard to imagine how procurement selects one tool
for an entire company. But this is already happening, and decision rights
are shifting from early adopters to technical leaders.

3 reasons AI disrupts Model Market Fit

AI can expose one or more variables in the Model Market Fit equation in
three ways:

1. A sharp reduction in average revenue per user (ARPU): AI-based tools
often automate and simplify something that used to be complex and
expensive. For example, if you charged $1,000 per year for a product
(such as specialized analytics or content creation), a new AI competitor
could lower the average price to $100 per year or even make the product
free (supported by advertising or data collection).

2. A reduction or fragmentation of TAM: Sometimes AI not only lowers
prices but also radically changes who qualifies as a paying customer.
Suppose your main market was companies that needed manual data
entry. If AI automates large volumes of data processing, the market itself
(i.e. the set of customers who need your old solution) shrinks dramatically.

3. A reduction in served available market (SAM): Even if the market does
not disappear and your ARPU stays the same, AI can produce new
leaders with network effects or entirely new approaches, making it harder
for incumbents to preserve (let alone grow) their share.

The chance to become a $100 million business still exists, but the path
may be different.

On one side there is risk, on the other there is opportunity.

Everything is happening very fast. I hope this makes you hurry a little.
Despite all the risks, huge opportunities are opening. Now you need to
analyze your product, market, channel, and model, and then carefully
examine how well each of the four elements currently works.
'''

# Create PDF and text outputs

def build_pdf(filename, text):
    output_path = OUTPUT_DIR / filename
    doc = SimpleDocTemplate(str(output_path), pagesize=LETTER,
                            rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=72)
    styles = getSampleStyleSheet()
    normal = ParagraphStyle(
        'Normal',
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        spaceAfter=10,
    )
    story = []
    for paragraph in text.split('\n\n'):
        if paragraph.strip() == '':
            continue
        paragraph = paragraph.replace('\n', '<br/>')
        story.append(Paragraph(paragraph, normal))
        story.append(Spacer(1, 6))
    doc.build(story)
    return output_path


def write_text(filename, text):
    output_path = OUTPUT_DIR / filename
    output_path.write_text(text, encoding='utf-8')
    return output_path

if __name__ == '__main__':
    write_text('PMF MFP EN.txt', pmf_mfp_text)
    write_text('PMF while AI EN.txt', pmf_while_ai_text)
    build_pdf('PMF MFP EN.pdf', pmf_mfp_text)
    build_pdf('PMF while AI EN.pdf', pmf_while_ai_text)
    print('Created translated PDFs and text files in', OUTPUT_DIR)
