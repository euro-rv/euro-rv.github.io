<!-- index.md -->

<style>
  .nav-buttons {
    text-align: center;
    margin-bottom: 1.5rem;
  }
  .nav-buttons a {
    display: inline-block;
    background-color: #15A9BA;
    color: white;
    padding: 0.5rem 1rem;
    margin-right: 0.5rem;
    text-decoration: none;
    border-radius: 4px;
    font-weight: bold;
  }
  .nav-buttons a:hover {
    background-color: #0f7f89;
  }

  @media (max-width: 640px) {
    .nav-buttons {
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
    }

    .nav-buttons a {
      margin-right: 0;
      width: 100%;
    }
  }

  h1 { color: #15A9BA; }
  h2 { color: #15A9BA; }
  h3 { color: #1C538E; }
</style>

<div class="nav-buttons">
  <a href="#description">Description</a>
  <a href="#call-for-contributions">Call for Contributions</a>
  <a href="#key-dates">Key Dates</a>
  <a href="#organizers">Organizers</a>
  <a href="#agenda-materials">Agenda & Materials</a>
</div>

<h3 style="color: #E48158;font-style: italic;">
  A half-day workshop on pathfinding research for next-generation RISC-V computing systems, <br>
  emphasizing hardware-software co-design across AI, HPC, and emerging workloads
</h3>

Venue located in conjunction with [the 59th IEEE/ACM International Symposium on Microarchitecture (MICRO 2026)](https://microarch.org/micro59/). Organized by [Barcelona Supercomputing Center (BSC)](https://www.bsc.es/) and [IMEC](https://www.imec-int.com/).

****  

## Key Dates {#key-dates}

- **Submission Deadline:** August 31 2026
- **Notification:** September 30, 2026
- **Workshop Date:** _To be defined_, but candidate dates are October 31 or November 1, 2026.

## Agenda & Workshop Materials {#agenda-materials}

{% include_relative agenda.html %}

## Workshop Description {#description}

The increasing demands and rapid evolution of AI, vector processing,
heterogeneous computing systems, and other emerging computational domains are
driving architectural innovation beyond the limits of today’s conventional
designs. Modern workloads in scientific computing, machine learning, data
analytics, graph processing, and adaptive systems require new approaches in
compute architectures, memory hierarchies, communication fabrics, resilience,
and hardware-software co-design. 

At the same time, RISC-V has evolved from an academic initiative into a widely
adopted open standard embraced by both industry and academia. Its open and
modular instruction set architecture provides unprecedented flexibility for
researchers and companies to explore domain-specific hardware acceleration,
custom instruction extensions, specialized vector and AI processing units, and
tightly integrated hardware-software optimizations. This openness significantly
lowers the barrier for architectural experimentation, enables faster innovation
cycles compared to traditional closed ISAs, and creates new opportunities for
collaborative research and industrial adoption. 

**Euro-RV** aims to bring together researchers exploring forward-looking ideas
for next-generation RISC-V computing systems. The workshop emphasizes
pathfinding research: exploratory concepts, early-stage architectures, and
enabling technologies that may shape future large-scale deployments and
computing platforms.

The workshop program will consist of a combination of invited talks, demos, and
discussion panels, together with contributions selected from the open call for
contributions.

We are committed to fostering an inclusive and diverse workshop community,
promoting broad participation among organizers and speakers, and continuously
improving our efforts through community feedback.

**Time & Location:** TBD — half-day workshop, co-located with [MICRO 2026](https://www.microarch.org/micro59/) in [Athens, Greece](https://maps.app.goo.gl/fDhQVDkrMd4HcB787).

## Call for Contributions {#call-for-contributions}

We welcome contributions spanning hardware, software, system architecture, and
cross-layer co-design. In addition to traditional paper and talk submissions,
we also strongly encourage demonstrations of mature technologies, prototypes,
and practical systems, in **demo** format.

### Topics of Interest

{% include_relative topics-of-interest.html %}

### Submission Instructions

- We welcome submissions of up to 2 pages (not including references). This is not a strict limit, but authors are encouraged to adhere to it if possible.
- All submissions must be in PDF format and should follow the main conference [LaTeX template](https://www.microarch.org/micro59/submit/micro59-latex-template.zip).
- Paper submission system will be defined in the coming weeks.
- Reviewing will be single-blind: please include all authors information. Changes to the authors list after submission won't be allowed.
- We welcome submissions that include parts of ongoing work intended for a future conference submission.

## Organizers {#organizers}

<style>
  .organizers {
    display: flex;
    flex-direction: column;
    gap: 2rem;
  }
  .organizer {
    display: flex;
    align-items: flex-start;
  }
  .organizer .photo-name {
    width: 120px;
    text-align: center;
    margin-right: 1.5rem;
  }
  .organizer .photo-name .text-role {
    color: #CFCFCF;
    font-weight: 300; // Light
  }
  .organizer .photo-name img {
    width: 120px;
    height: auto;
    border-radius: 8px;
    display: block;
    margin-bottom: 0.5rem;
  }
  .organizer .photo-name p {
    margin: 0;
    font-weight: bold;
  }
  .organizer .bio {
    flex: 1;
  }
  .organizer .bio p {
    margin: 0.25rem 0;
  }
  .organizer .bio p:first-child {
    margin-top: 0;
  }

  @media (max-width: 640px) {
    .organizer {
      flex-direction: column;
    }

    .organizer .photo-name {
      align-items: center;
      display: flex;
      gap: 0.75rem;
      margin-bottom: 0.75rem;
      margin-right: 0;
      text-align: left;
      width: 100%;
    }

    .organizer .photo-name img {
      flex: 0 0 auto;
      margin-bottom: 0;
      width: 72px;
    }

    .organizer .bio {
      width: 100%;
    }
  }
</style>

<div class="organizers">

  {% for organizer in site.data.organizers %}
  <div class="organizer">
    <div class="photo-name">
      <img src="{{ organizer.photo | relative_url }}" alt="{{ organizer.name }}">
      <p>{{ organizer.name }}</p>
      <p class="text-role">({{ organizer.role }})</p>
    </div>
    <div class="bio">
      <p><i>{{ organizer.affiliation }}</i></p>
      <p>{{ organizer.bio }}</p>
    </div>
  </div>
  {% endfor %}

</div>
