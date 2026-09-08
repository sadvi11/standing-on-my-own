# Setup — the decisions I did not make for you

The site works now. These four are yours, and three of them get harder the
longer you leave them.

---

## 1. The name and URL — decide before you share it anywhere

Right now: **`sadvi11.github.io/standing-on-my-own`**

The repository name is the URL. Renaming is **free today** and expensive once
anyone has linked to it, so if "Standing on my own" is not the name you want,
change it now:

```
Repository → Settings → rename
```

Then update the four `/standing-on-my-own/` paths in `index.html`,
`about.html` and `build.py`.

**A custom domain** costs about $15/year and is worth it if you are serious
about the TEDx and earning goals — `sadvishar.ma` reads as a body of work,
`sadvi11.github.io/standing-on-my-own` reads as a side project. GitHub Pages
supports custom domains free; you only pay the registrar.

Do this before writing thirty pieces, not after.

---

## 2. Should this carry your name?

You write about emotional independence. Your other site is a technical
portfolio a recruiter reads.

Right now they share a GitHub account, which means a determined person connects
them in about a minute. That may be exactly what you want — writing well in
public is an asset, and speakers get booked because someone found their
writing.

But it is a decision, and it is easier made now than unwound later. If you want
them separate, that means a different GitHub account and a custom domain.

I have not linked the two sites to each other. That is deliberate; add the link
if you want it.

---

## 3. Email list — do this early, it compounds

An email list is the only audience you own. Followers belong to a platform that
can change its algorithm or disappear; an email list moves with you.

Every route to earning from writing — a book, a course, coaching, paid
speaking — runs through a list. And a list of 200 people who chose to hear from
you is worth more than 5,000 followers who did not.

Two free options, both a paste-in form:

| | Free tier | Notes |
|---|---|---|
| **Buttondown** | 100 subscribers | Plain, writer-focused, easy to export |
| **MailerLite** | 1,000 subscribers | More features, more setup |

Either gives you an HTML snippet. Paste it into the `.subscribe` block in
`index.html`, replacing the placeholder paragraph.

**Start it before you have readers.** Adding a form on day one costs nothing.
Adding it after fifty pieces means fifty pieces' worth of readers who came, read
and left with no way to hear from you again.

---

## 4. The thesis on the front page is a placeholder

The box under the title currently holds a sentence I wrote to show the shape.
**Replace it with yours.**

This matters more than it looks, and it is the direct line to the TEDx goal. A
TEDx talk is one idea worth spreading — not a topic, an *idea*, stated as a
claim someone could disagree with.

"Emotional independence" is a topic. Something like *"needing people is not
dependence; being unable to hold your own position while you need them is"* is
an idea — it makes a claim, and a reasonable person might argue with it.

You do not need the final version today. You need a first version you can
revise in public, because a hundred short pieces circling one claim is how a
talk gets built. Writing daily without a through-line produces a hundred pieces
and no talk.

Revise it as your thinking changes. That the box changes over time *is* the
work being visible.

---

## Adding a piece

**In the browser:** `posts/` → Add file → Create new file → name it
`something.md` → paste the front matter from `TEMPLATE.md` → commit. The Action
rebuilds and publishes. Works from a phone.

**Locally:** `cp posts/TEMPLATE.md posts/whatever.md`, write, `python3 build.py`,
commit.

The build fails loudly on a malformed date or a missing title, so a typo does
not quietly sort your archive wrongly.
