<!-- index.md -->

<style>
  .nav-buttons {
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

![Euro-RV Workshop Logo](euro-rv-logo.svg){: width="700px" }

<h3 style="color: #E48158;font-style: italic;">
  A half-day workshop on pathfinding research for next-generation RISC-V computing systems, <br>
  emphasizing hardware-software co-design across AI, HPC, and emerging workloads
</h3>

**October 31 or November 1, 2026, Athens, Greece**  
**In conjunction with [the 59th IEEE/ACM International Symposium on Microarchitecture (MICRO 2026)](https://microarch.org/micro59/)**  
**Organized by [Barcelona Supercomputing Center (BSC)](https://www.bsc.es/) and [IMEC](https://www.imec-int.com/)**

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

Topics include, but are not limited to:

- **Vector and General-Purpose Architectures**
  - Vector processing architectures
  - Reconfigurable VPUs and adaptive execution engines
  - Memory management accelerators
  - Novel ISA and microarchitectural extensions
  - Energy-efficient and power-aware architectures
  - Scalable manycore and heterogeneous systems
- **High-Performance Computing**
  - Scalable HPC architectures and exascale systems
  - HPC-oriented RISC-V processors and accelerators
  - Communication-efficient distributed computing systems
  - Runtime systems and compiler optimizations for HPC
  - Hardware/software co-design for scientific computing
  - Energy-efficient HPC systems and sustainability
  - Heterogeneous HPC platforms integrating CPUs, GPUs, and AI accelerators
  - Fault tolerance, resilience, and reliability in large-scale systems
- **AI and Accelerators**
  - On-device learning and refinement hardware
  - Training-aware AI accelerators
  - Scalable AI communication infrastructures
  - Distributed and multi-AIPU systems
  - Sparse and irregular workload acceleration
  - AI hardware/software co-design
- **Reliability and System Architecture**
  - Reliability, Availability, and Serviceability (RAS)
  - Fault tolerance and resilient architectures
  - Runtime monitoring and adaptive systems
  - Security and trustworthy architectures
- **Hardware-Software Co-Design**
  - Compiler and runtime innovations
  - Emerging software stacks for heterogeneous systems
  - Application-driven architectural exploration
  - Performance modeling and simulation
  - Hardware/software co-design methodologies
  - Programming models for future architectures
- **Emerging Applications**
  - Scientific computing
  - Data analytics and databases
  - Genomics and bioinformatics
  - Adaptive and autonomous systems
  - Foundation model infrastructure
  - HPC-AI convergence

### Submission Instructions

- We welcome submissions of up to 2 pages (not including references). This is not a strict limit, but authors are encouraged to adhere to it if possible.
- All submissions must be in PDF format and should follow the main conference [LaTeX template](https://www.microarch.org/micro59/submit/micro59-latex-template.zip).
- Paper submission system will be defined in the coming weeks.
- Reviewing will be single-blind: please include all authors information. Changes to the authors list after submission won't be allowed.
- We welcome submissions that include parts of ongoing work intended for a future conference submission.

## Key Dates {#key-dates}

- **Submission Deadline:** August 31 2026
- **Notification:** September 30, 2026
- **Workshop Date:** _To be defined_, but candidate dates are October 31 or November 1, 2026.

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
</style>

<div class="organizers">

  <div class="organizer">
    <div class="photo-name">
      <img src="{{ 'pics/julian-pavon.jpg' | relative_url }}" alt="Julian Pavon">
      <p>Julian Pavon</p>
    </div>
    <div class="bio">
      <p><i>Barcelona Supercomputing Center (BSC)</i></p>
      <p>Julian Pavon is a Research Engineer at the Barcelona Supercomputing Center. He earned his PhD from the Universitat Politècnica de Catalunya. His research interests include general-purpose computer architecture, vector architectures, and hardware-software co-design for data-intensive workloads. His research is published in top-tier venues, including ISCA, HPCA, MICRO and CAL, among others. Julian has worked on designing and developing different hardware modules for multiple manufactured RISC-V cores.</p>
    </div>
  </div>

  <div class="organizer">
    <div class="photo-name">
      <img src="{{ 'pics/nitesh-narayana-gs.jpg' | relative_url }}" alt="Nitesh Narayana GS">
      <p>Nitesh Narayana GS</p>
    </div>
    <div class="bio">
      <p><i>Barcelona Supercomputing Center (BSC)</i></p>
      <p>Nitesh Narayana GS is currently a Senior Research Engineer in the Computer Architecture for Parallel Paradigms group at the Barcelona Supercomputing Center and a PhD student at Universitat Politècnica de Catalunya. Before that, he received his Bachelor and Master of Technology Dual Degree in Computer Engineering and Design from the Indian Institute of Information Technology Design and Manufacturing (IIITDM) Kancheepuram, Tamil Nadu, India. His current research focuses on energy-efficient architectures, ranging from microarchitectural to system-level optimisations.</p>
    </div>
  </div>

  <div class="organizer">
    <div class="photo-name">
      <img src="{{ 'pics/negin-mahani.png' | relative_url }}" alt="Negin Mahani">
      <p>Negin Mahani</p>
    </div>
    <div class="bio">
      <p><i>Barcelona Supercomputing Center (BSC)</i></p>
      <p>Negin Mahani is a Senior Researcher and Associate Technical Coordinator for the six Technical Areas of DARE, a flagship EuroHPC project, at the Barcelona Supercomputing Center (BSC). Her research focuses on GPU microarchitecture, deep learning acceleration, in-memory computing, and hardware–software co-design. She received her Ph.D. in Computer Architecture from Sharif University of Technology, and her M.Sc. and B.Sc. from the University of Tehran and Bahonar University of Kerman, respectively. She has also held an academic position as tenure-track Assistant Professor and served in faculty coordination and academic leadership roles in Bahonar University, Zarand Faculty.</p>
    </div>
  </div>

  <div class="organizer">
    <div class="photo-name">
      <img src="{{ 'pics/sourav-sengupta.png' | relative_url }}" alt="Sourav Sengupta">
      <p>Sourav Sengupta</p>
    </div>
    <div class="bio">
      <p><i>Interuniversity Microelectronics Centre (IMEC)</i></p>
      <p>Sourav Sengupta is the R&amp;D Group Leader for Future System Architecture (FSA) at CSA, imec. He comes from an interdisciplinary background with a PhD in Computer Science (2014), a Master's in Pure Mathematics (2008), and a Bachelor's in Electronics Engineering (2006). With over 15 years of research experience and more than 10 years of teaching across four countries, he brings a global and cross-disciplinary perspective to innovation and leadership. Sourav is a technical coordinator in the flagship EuroHPC project DARE, leading one of the six Technical Areas, as well as an IMEC team designing and developing scale-out performance model for virtual integration and pathfinding.</p>
    </div>
  </div>

  <div class="organizer">
    <div class="photo-name">
      <img src="{{ 'pics/arindam-mallik.png' | relative_url }}" alt="Arindam Mallik">
      <p>Arindam Mallik</p>
    </div>
    <div class="bio">
      <p><i>Interuniversity Microelectronics Centre (IMEC)</i></p>
      <p>Arindam Mallik is the Department Director for Compute System Architecture (CSA) at IMEC. He is a technologist enabling HW-SW co-design at the cross-point of AI algorithms, computer architecture, and novel technology solutions. Arindam has spent the past 20 years pushing the boundaries of technology research to provide novel solutions with a direct impact on the semiconductor industry. He has authored or co-authored more than 100 papers in international journals and conference proceedings and holds a number of relevant patents. He received M.S. and PhD degrees in Electrical Engineering and Computer Science from Northwestern University, USA in 2004 and 2008, respectively.</p>
    </div>
  </div>

  <div class="organizer">
    <div class="photo-name">
      <img src="{{ 'pics/pablo-balbi.jpeg' | relative_url }}" alt="Julian Pavon">
      <p>Pablo Balbi</p>
    </div>
    <div class="bio">
      <p><i>Barcelona Supercomputing Center (BSC)</i></p>
      <p>Julian Pavon is a Research Engineer at the Barcelona Supercomputing Center. He earned his PhD from the Universitat Politècnica de Catalunya. His research interests include general-purpose computer architecture, vector architectures, and hardware-software co-design for data-intensive workloads. His research is published in top-tier venues, including ISCA, HPCA, MICRO and CAL, among others. Julian has worked on designing and developing different hardware modules for multiple manufactured RISC-V cores.</p>
    </div>
  </div>

</div>

## Agenda & Workshop Materials {#agenda-materials}

<p><em>The workshop agenda will be announced after the submission deadline. Check back for invited talks, contributed presentations, demos, and panel sessions.</em></p>

<style>
  table.agenda { width:100%; border-collapse: collapse; table-layout: fixed; }
  table.agenda th, table.agenda td { border: 2px solid #bbb; padding: 8px; text-align:left; }
  table.agenda thead { background:#15A9BB; color:#000; }
  table.agenda tbody { color:#000; }
  table.agenda tbody.session tr:nth-child(odd)  { background:#ffffff; }
  table.agenda tbody.session tr:nth-child(even) { background:#f2f8fa; }
  table.agenda tbody.break tr td {
    background:#d8ebe7; font-weight:700; text-align:center;
  }
</style>

<table class="agenda">
  <colgroup>
    <col style="width:12%;">
    <col style="width:32%;">
    <col style="width:18%;">
    <col style="width:38%;">
  </colgroup>

  <thead>
    <tr>
      <th>Time</th>
      <th>Speaker</th>
      <th>Domain</th>
      <th>Title</th>
    </tr>
  </thead>

  <tbody class="session">
    <tr>
      <td colspan="4" style="text-align:center; font-style:italic;">Agenda to be announced</td>
    </tr>
  </tbody>
</table>
