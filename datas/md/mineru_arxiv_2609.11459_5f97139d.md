# Bottom-up Synthesis of Metastable 2D Hexagonal Copper(I) Iodide on Monolayer and within Bilayer Graphene

David Kaiser<sup>a</sup>, Guobin Jia<sup>b</sup>, Janis Köster<sup>c</sup>, Sadegh Ghaderzadeh<sup>d</sup>, Christian E. Halbig<sup>e</sup>, Siegfried Eigler<sup>e</sup>, Andrey Turchanin<sup>a</sup>, Benjamin Dietzek-Ivanšić<sup>b,f</sup>, Arkady V. Krasheninnikov<sup>g</sup>, Jonathan Plentz<sup>b</sup>, Elena Besley<sup>d</sup>, Ute Kaiser<sup>c\*</sup>

<sup>a</sup> Institute of Physical Chemistry, Friedrich Schiller University Jena, 07743 Jena, Germany <sup>b</sup> Leibniz Institute of Photonic Technology (Leibniz-IPHT), 07745 Jena, Germany

<sup>c</sup> Institute for Quantum Optics and Central Facility Materials Science Electron Microscopy, Ulm University, Albert-Einstein-Allee 11, 89081 Ulm, Germany

<sup>d</sup> School of Chemistry, University of Nottingham, University Park, Nottingham NG7 2RD, UK

<sup>e</sup> Institute of Chemistry and Biochemistry, Freie Universität Berlin, Altensteinstraße 23a, 14195 Berlin, Germany

<sup>f</sup> Leibniz Institute of Surface Engineering (IOM), Permoserstr. 15, 04318 Leipzig, Germany <sup>g</sup> Institute of Ion Beam Physics and Materials Research, Helmholtz-Zentrum Dresden-Rossendorf, 01328 Dresden, Germany.

\*Corresponding author: ute.kaiser@uni-ulm.de

Copper(I) iodide (CuI) is a wide-bandgap semiconductor crystallizing in the 3D γ- phase under ambient conditions; its layered van der Waals bulk phase (β-CuI) is stable only between 643 and 673 K. The two-dimensional (2D) h-CuI form has been obtained via liquid-phase exfoliation of mechanochemically prepared precursors and via encapsulation between graphene sheets, whereas bottom-up growth of 2D h-CuI on open surfaces has not yet been demonstrated. Here, we report a vaporphase synthesis of h-CuI directly on low-defect, large-area monolayer and within bilayer reduced oxo-graphene (r-oxo-G) at low temperatures. Using a copper TEM grid as the solid-state precursor for copper, HI-vapor exposure at $40 \%$ initiates nucleation, while annealing at 180 °C promotes the growth of extended h-CuI domains. Aberration-corrected HRTEM resolves the atomic structure, local twist angles, and lattice anisotropy of the CuI/r-oxo-G nanohybrid, while STEM-EDX yields a Cu:I ratio consistent with 1:1. First-principles calculations show that van der Waals adhesion to graphene stabilizes the supported hexagonal layer. Under the presented low-temperature precursor conditions, pathways for nucleation of the γ-phase are not available, allowing the hexagonal phase to form selectively at the graphene interface. Ab initio molecular dynamics simulations show that the heterostructure retains its hexagonal lattice order at 600 K, including on an open monolayer graphene support. The lateral extent of the growth is limited mainly by remaining interfacial adsorbates. These results establish a route to metastable 2D h-CuI on a chemically inert graphene template, which may be useful for widebandgap electronic and optoelectronic devices.

Two-dimensional (2D) van der Waals (vdW) heterostructures provide a versatile platform for combining materials with different bonding motifs, dimensionalities, and functionalities [1]. In particular, the integration of covalently bonded 2D templates with ionic compounds enables nanohybrid structures that are difficult to realize in bulk form [2–5]. While intrinsically stable 2D materials are now well established [6], increasing attention is being directed toward non-vdW compounds that become metastable in the 2D limit [7,8]. Their stabilization often relies on confinement or interfacial interactions, for example within bilayer graphene or other 2D matrices [4,8–10]. Such approaches have enabled ultrathin silica glass [4], gallium nitride [9], and metal halides [11–13], while graphene encapsulation can additionally protect fragile structures during in situ electron microscopy [14].

Hexagonal copper(I) iodide (h-CuI) is the two-dimensional form of copper iodide, identified by Bädeker in 1907 as the first transparent conductor [15]. 2D h-CuI combines a wide bandgap, optical transparency, p-type conductivity, and exceptionally low thermal conductivity [16–19], and monolayers have been proposed for transparent electronics, photodetectors, sub-10 nm field-effect transistors, and mechanically compliant wearable devices [17–20]. Under ambient conditions, however, CuI adopts the non-layered zincblende γ-phase, whereas the layered $\beta - p h a s e$ , the bulk parent of h-CuI, is an equilibrium phase only within the narrow temperature range of 643–673 K and reverts to γ-CuI on cooling [16,21]. Computational screening predicted a freestanding 2D phase [22], and phonon calculations indicate that it is dynamically stable [17,23]. Thermodynamically, however, the layered stacking lies 3.0–3.4 $\mathsf { m e V } / \mathsf { A } ^ { 2 }$ above γ-CuI and is separated from it by a barrier of about 13 $\mathsf { m e V } / \mathsf { A } ^ { 2 }$ for the reconstructive, bond-breaking transformation between the layered and zinc-blende stackings [21]. Thus, h-CuI represents a metastable but kinetically trappable 2D phase.

Direct growth of this layered phase on an open surface has remained elusive. Physical vapor deposition from CuI powder yields the cubic γ-phase even on van der Waals templates, including $\mathsf { S i O } _ { 2 } / \mathsf { S i }$ and ${ \sf W S e } _ { 2 } / { \sf W S } _ { 2 }$ monolayers [24], while close-distance sublimation on sapphire, Si, GaAs, and GaN produces epitaxial γ-CuI containing only a transient 12R polytype embedded in the γ matrix [25], a stacking that has been ruled out as the true layered phase [21]. The layered phase has instead been obtained through confinement or top-down processing. Mustonen et al. precipitated h-CuI inside bilayergraphene sandwiches, where the confined gap acts as a nanoreactor [26]; notably, no h-CuI formed on the open monolayer regions of the same samples. $\beta \mathrm { - C u l }$ nanocrystals have likewise been stabilized within reduced-graphene-oxide membranes [27]. Peng et al. obtained uncovered h-CuI flakes by mechanochemical grinding of $\gamma \mathrm { - C u l }$ in water followed by liquid-phase exfoliation [23]; these flakes persist under ambient conditions but have no epitaxial relationship to a substrate. Ab initio molecular dynamics simulations further showed that a bare monolayer loses structural integrity at 600 K, whereas grapheneencapsulated 2D h-CuI remains stable [28]. Bottom-up growth of the layered phase directly on an open surface has not been reported.

Here, we demonstrate the bottom-up growth of 2D h-CuI directly on open monolayer and within bilayer reduced oxo-graphene. The copper TEM grid serves as the solid-state copper source, while HI vapor provides iodine and simultaneously reduces the oxographene template. 80 kV Cc/Cs-aberration-corrected HRTEM resolves the atomic structure, local epitaxial alignment, and uniaxial lattice adaptation of the h-CuI/graphene heterostructure, while STEM-EDX establishes a Cu:I ratio consistent with 1:1. DFT calculations quantify the van der Waals adhesion and identify h-CuI on an open graphene surface as thermodynamically metastable, whereas AIMD simulations show that the hexagonal lattice is retained up to 600 K. Experimentally, extended growth correlates with removal of interfacial adsorbates, identifying interface cleanliness as a key factor controlling the lateral domain size. These results establish a route to metastable 2D h-CuI on a chemically inert graphene template.

## RESULTS AND DISCUSSION

Fig. 1 summarizes the synthesis, a two-step process carried out entirely on a single grid (Methods; Supporting Information, Section S1). The starting material is a film of oxofunctionalized graphene (oxo-G) on a standard copper transmission-electron-microscopy (TEM) grid. In the first step, the film is exposed to hydrogen iodide (HI) vapor at $40 \%$ where HI serves a dual purpose: it reduces the oxo-G to reduced oxo-graphene (r-oxo-G) [30], and it attacks the copper of the grid, the solid-state copper source of the synthesis. Since the vapor comes from an aqueous HI solution and the reduction of the oxo-groups releases water, a thin adsorbed film is present at the interface during this step (Section S1). The copper released from the grid crosses the graphene by surface diffusion, on a potential energy landscape flat enough for copper adatoms to migrate anomalously at room temperature [32], and meets the iodine adsorbed during the HI treatment, where small hexagonal CuI (h-CuI) crystallites nucleate. The copper originates solely from the grid: a control synthesis on a gold (Au) TEM grid, under otherwise identical conditions, yields no h-CuI (Supporting Information, Section S1). In the second step, annealing at 180 °C grows the crystallites into extended, van der Waals-epitaxial domains. Every step takes place on the original graphene substrate, so the route needs no transfer step and no sacrificial polymer; the same two-step route also forms h-CuI within bilayer graphene, by intercalation. The growth mechanism and the selection of the hexagonal phase are discussed in detail below.

## Template characterization and substrate morphology

The structural integrity and morphology of the oxo-G template were first examined prior to HI treatment and thermal annealing. Overview TEM imaging [Fig. 2(a)] confirms the formation of continuous, large-area oxo-G membranes spanning the copper TEM grid support. 80 kV $\complement _ { \mathsf { c } } / \complement _ { \mathsf { s } } .$ -corrected high-resolution TEM (HRTEM) reveals a heterogeneous substrate morphology consisting of monolayer, bilayer, and trilayer regions. A representative boundary between monolayer and trilayer areas is shown in Fig. 2(b), with the corresponding layer numbers confirmed by the fast Fourier transform (FFT) patterns shown in the insets.

![](images/adc1f4d34e3144a107a32a16f829f9a5ff09811a317fc7a127cd48fc33791e79.jpg)  
Figure 1. h-CuI synthesis on graphene supported by a copper TEM grid. In the first step, HI treatment at $4 0 ~ ^ { \circ } \bar { \mathsf { C } }$ forms, through van der Waals stabilization, monolayer h-CuI on graphene; during this step the oxo-graphene template (oxo-G) is reduced to r-oxo-G simultaneously. Annealing at $1 8 0 ^ { \circ } \mathsf { C }$ then promotes the epitaxial growth of extended h-CuI crystals on graphene. The atom types are indicated at the bottom.

High-resolution lattice images of monolayer and bilayer regions [Figs. 2(c) and 2(e)] demonstrate pronounced long-range crystalline order within the oxo-G sheets, despite minor amorphous surface residues that are typical of liquid-phase exfoliation and transfer processes. In bilayer regions, rotational misalignment between the two constituent sheets gives rise to distinct moiré superlattices [Fig. 2(e)]. The FFT analysis in Fig. 2(f) shows two discrete sets of sharp hexagonal reflections, labeled G and G′, corresponding to a relative twist angle of $1 6 . 7 ~ \pm ~ 1 . 0 ^ { \circ }$ . These well-defined crystallographic signatures demonstrate that the oxo-G retains the lattice periodicity required to act as a robust template for van der Waals (vdW) epitaxy. The coexistence of monolayer and bilayer regions from the same exfoliation batch on the same grid further enables a direct comparison of h-CuI growth on SLG and BLG.

## Vapor-phase growth on monolayer graphene: HRTEM analysis

We first examined h-CuI formation on samples that received HI treatment at $40 \%$ without subsequent annealing. HRTEM imaging revealed the nucleation of discrete h-CuI crystallites of about 5 nm on monolayer and bilayer r-oxo-G. Fig. 3(a) shows a crystallite epitaxially grown on monolayer r-oxo-G. FFT analysis of the adjacent substrate confirms the monolayer nature of the graphene template [inset, Fig. 3(a)], while the heterostructure FFT [Fig. 3(b)] shows the white graphene reflections G together with a distinct set of red reflections from h-CuI. Because the small lattice mismatch can bring an h-CuI reflection close to a graphene spot, the layer number is independently confirmed at an adjacent

![](images/a084b7f972eaca3a6c1c3ae81e974a392f632e50169cd561d360b0ef3e66f9e3.jpg)

![](images/6ece964cd2f4ad573bdf30ac339613509eef8f090dffdb6db64e6c47de89f7fb.jpg)

![](images/4f16c7c2db70ff5e3797c0724f073c3b80610d037cb8684e7319ff96e879df7d.jpg)

![](images/fc654aa06a837b2e85e2205168af6dbbcd2dabb7e068c8bd386f5ff157525733.jpg)

![](images/8a549b2dbc3cd12446a846c4a32a13afcf9de3e5310ec5dc691058358b7c5338.jpg)

![](images/9df5e6921f2850aca996e4fcf15f7520d158c025bf1d6f50c373532e68a58bb3.jpg)  
Figure 2. Structural and crystallographic characterization of oxo-G templates. (a) Lowmagnification $\complement _ { \mathsf { c } } / \complement _ { \mathsf { s } }$ -corrected HRTEM overview of oxo-G flakes suspended on a TEM grid, showing characteristic folds and local thickness variations. (b) $\mathsf { C } _ { \mathsf { c } } / \mathsf { C } _ { \mathsf { s } } \mathsf { - c o r r e c t e d }$ HRTEM image of the interface between a monolayer domain (top) and a trilayer domain (bottom), indicated by the white line; the insets show the corresponding FFT patterns. (c) Representative $\complement _ { \mathsf { c } } / \complement _ { \mathsf { s } } .$ -corrected HRTEM image of a monolayer oxo-G region; the inset shows an atomic-resolution view of the hexagonal lattice. (d) FFT pattern obtained from the region shown in (c), displaying the reflections of a single graphene lattice, labeled G and marked by the dashed circle. (e) $\complement _ { \mathrm { c } } / \complement _ { \mathrm { s } } .$ -corrected HRTEM image of a rotationally misaligned bilayer region exhibiting a moiré superlattice, magnified in the inset. (f) Corresponding FFT pattern of the bilayer region, showing two sets of hexagonal reflections, labeled G and $\mathbf { G ^ { \prime } } ,$ , with a relative twist angle of $1 6 . 7 \pm 1 . 0 ^ { \circ }$ . All data were acquired at an accelerating voltage of 80 kV.

graphene-only region [inset, Fig. 3(a)]. This region shows a single set of first-order graphene reflections with no moiré pattern, which identifies the substrate as monolayer. The $h { \mathrm { - C u l } }$ lattice vectors b1, b2, b3 are determined from the HRTEM image by fitting twodimensional Gaussians to the atomic columns [31], while the graphene primitive vectors a1, a2, a3 are obtained from the corresponding FFT and serve as the internal length reference; all measured lattice vectors and twist angles are tabulated in Table S1. In every annealed crystallite the largest of the three lattice vectors reaches the commensurate graphene superlattice value of $\mathtt { a } \sqrt { 3 } \approx 0 . 4 2 6$ nm, with 0.426–0.427 nm, and the smallest stays at the freestanding $h { - } \mathsf { C u l }$ value of 0.419 nm, with 0.418–0.421 nm — each within the measurement uncertainty of $\pm { \ : 0 . 0 0 2 }$ nm (Table S1). This pattern holds on monolayer and within bilayer graphene alike; the adaptation of the individual crystallites is therefore characterized below from their anisotropy. The epitaxial twist angle is defined as $\mathsf { \Omega } \mathsf { \Lambda } \Theta = | 3 0 ^ { \circ }$ $- \Delta |$ , where $\Delta$ is the angle between the h-CuI lattice vector b3 and the nearest graphene primitive vector a. Physically, the $30 ^ { \circ }$ offset reflects the energetically preferred registry in which the iodine atoms occupy the centers of the graphene hexagons [26]; this hexagoncenter sublattice is rotated by $30 ^ { \circ }$ relative to the graphene atomic lattice, so $\boldsymbol \theta \ : = \ : 0$ corresponds to perfect epitaxial lock-in (Section S2c). For the nucleus shown in Fig. 3, this yields $\mathsf { \Omega } \Theta = 1 1 . 9 ^ { \circ } \pm 1 . 0 ^ { \circ }$ . Thermal annealing at $1 8 0 ^ { \circ } \mathsf { C }$ significantly improves crystallinity and promotes lattice relaxation. Post-annealing HRTEM imaging [Fig. 3(d)] reveals increased domain sizes and sharper diffraction spots [Fig. 3(e)], which again show the $h \mathrm { - }$ CuI reflections together with those of graphene. The monolayer assignment is confirmed again by a separate windowed FFT of an adjacent graphene-only region [inset, Fig. 3(d)], which shows a single set of first-order graphene reflections without a moiré pattern, ruling out a bilayer. The measured lattice vectors $\mathsf { b } _ { 1 } = 0 . 4 2 1 \pm 0 . 0 0 2$ nm, $\mathsf { b } _ { 2 } = 0 . 4 2 5 \pm 0 . 0 0 2$ nm and $\mathsf { b } _ { 3 } ~ = ~ 0 . 4 2 7 ~ \pm ~ 0 . 0 0 2$ nm span the range between the freestanding and the commensurate value.

To characterize how the h-CuI lattice adapts to the graphene template, we compare the measured lattice vectors with the commensurate graphene superlattice period $( { \mathsf { a } } { \sqrt { 3 } } \approx$ 0.426 nm). The adaptation is uniaxial: along one direction an h-CuI vector matches the substrate period, while the perpendicular vector stays close to the intrinsic h-CuI value and retains a residual mismatch of about 1.4% (from the initial 1.67% lattice mismatch). Across the measured crystals this leaves a small directional anisotropy — the ratio of the longest to the shortest lattice vector — of 1.014–1.019 (Table S1). In our open monolayer the perpendicular direction is not contracted below the intrinsic h-CuI value, i.e. the uniaxial adaptation proceeds without a perpendicular (Poisson) compression, whereas Mustonen et al. [26] report a comparable anisotropy for graphene-encapsulated 2D h-CuI. The energetics that select this uniaxial adaptation — the registry (corrugation) energy gained on commensuration against the elastic strain cost, and the lower bound it places on the interfacial corrugation — are analyzed in detail in the Growth mechanism and phase selection section.

## Intercalation and growth within bilayer graphene

The presence of both monolayer and bilayer graphene flakes in the oxo-G substrate enables a direct comparative study of h-CuI growth under identical experimental conditions. Following HI treatment at $4 0 \ ^ { \circ } \mathsf { C } ,$ , h-CuI nucleation is also observed within bilayer regions. HRTEM imaging [Fig. 4(a)] reveals intercalated h-CuI crystallites between two graphene sheets. The bilayer nature is confirmed by the FFT of the adjacent region [inset, Fig. 4(a)], showing the two hexagonal graphene lattices G and $\mathbf { G ^ { \prime } }$ with a relative twist angle of $2 6 . 0 ^ { \circ } ~ \pm ~ 1 . 0 ^ { \circ }$ The heterostructure FFT [Fig. 4(b)] displays triple-lattice symmetry from G, G′, and the red h-CuI reflections. For this specific crystallite, h-CuI shows epitaxial deviation angles of $\mathsf { \Omega } \theta = 1 4 . 4 ^ { \circ } \pm 1 . 0 ^ { \circ }$ to G and $\Theta ^ { \prime } = 1 9 . 6 ^ { \circ } \pm 1 . 0 ^ { \circ }$ to G′. Atomic position mapping yields lattice vectors of b $_ 1 = 0 . 4 1 6 \pm 0 . 0 0 2$ nm, $\mathsf { b } _ { 2 } = 0 . 4 1 6 \pm 0 . 0 0 2$ nm, and $\mathsf { b } _ { 3 } = 0 . 4 1 9 \pm 0 . 0 0 2$ nm, corresponding to $\mathsf { A } _ { \mathsf { b } } = 1 . 0 0 7 \pm 0 . 0 0 4$ . These values correspond to an essentially isotropic crystallite. We attribute the near-absence of in-plane anisotropy to the early stage of growth: the nucleus is small and has a high edge-to-area ratio, so its lattice has not yet developed the directional adaptation that characterizes larger, fully grown domains. The extracted constants therefore remain close to the intrinsic 2D h-CuI value of $0 . 4 1 9 \pm 0 . 0 0 2$ nm. Thermal annealing at $1 8 0 ~ ^ { \circ } \mathsf { C }$ promotes the further growth of these intercalated domains [Fig. 4(d)]. In the observed samples, $h { \mathrm { - C u l } }$ often achieved near-perfect alignment with one graphene layer, here $\mathbf { G ^ { \prime } } ,$ for which $\Theta ^ { \prime } \approx 0 ^ { \circ }$ and the diffraction spots are rotated by $30 ^ { \circ }$ , while it maintained a twist angle of $\mathsf { \Omega } \theta = 2 1 . 7 ^ { \circ } \pm 1 . 0 ^ { \circ }$

![](images/b4743576a71b2072479d5d41d2682460b5a44144b0c57f83575fb7f92f9616bb.jpg)

![](images/1cea226fd147f53bd6c6151e1183b5717399109b81357856d71e37e43faf9445.jpg)

![](images/40d9f8fac0721a778315c65f4dda6cd828b1cf72364817819510139cdabd5a69.jpg)

![](images/295203db34fafdbbae25bc654b5c5c5fc162dab677f22ddeaa51d5981ad6e22b.jpg)

![](images/051dc853185fb0e698060d117cc15b2ec064d547f38e8d6cfc8f19f87c8de05c.jpg)

![](images/3508d6bee5b05550eee5f7fb17635f3cbe0ec42b8ff1c57ced96af131d226794.jpg)  
Figure 3. Vapor-phase synthesis and vdW-epitaxial growth of h-CuI on monolayer graphene. (a) C /C -corrected HRTEM image (80 kV) of an h-CuI crystallite (\~5 nm) nucleated on monolayer graphene following HI treatment at $4 0 ~ ^ { \circ } \mathrm { { C } }$ . The inset FFT of the adjacent substrate confirms the monolayer nature of the graphene template (G). (b) FFT of the heterostructure region displaying commensurate reflections from graphene (G, white) and h-CuI (red circles). (c) Schematic of the epitaxial registry at $4 0 \ ^ { \circ } \mathsf { C } \colon h – \mathsf { C u l }$ on SLG with iodine atoms occupying graphene hollow sites at a twist angle of $\textsf { \textsf { \textsf { \textsf { \textsf { \textsf { \varepsilon } } } } } } = \textsf { 1 1 . 9 ^ { \circ } } \pm \textsf { 1 . 0 ^ { \circ } }$ (Sample 1). Views are reconstructed from experimental lattice vectors $( \mathsf { b } _ { 1 } , \mathsf { b } _ { 2 } , \mathsf { b } _ { 3 } )$ and measured twist angles. (d) HRTEM image of an expanded $h { - } \mathsf { C u l }$ domain (up to about 30 nm) on monolayer graphene after thermal annealing at $1 8 0 ^ { \circ } \mathsf { C }$ . (e) Corresponding FFT showing enhanced intensity and sharpness of h-CuI reflections, indicating improved crystalline quality and lattice relaxation post-annealing $( \Theta = 2 1 . 2 ^ { \circ } \pm 1 . 0 ^ { \circ }$ Sample 2). (f) Structural schematic of the annealed heterostructure, illustrating the evolution of the moiré superlattice.

![](images/3292a27dbbe6355f6dae6da1098d3e491aba9a38aef75c8be565bd2b2f32539b.jpg)

![](images/430dd2e075df8345b40b67b811d7489f8e2ada80ea407a3bd7c5e982836b636a.jpg)

![](images/cab28cfc1f746ecc3ad82cd56093afdc030b2bf9f1a74861320247c6296ff4ad.jpg)

![](images/0631819375af1e94d6bb55877a21f15abb86ac26d796a1fbf21af9ef3466db94.jpg)

![](images/252c084b748c3a3e2d6fc6f5578a898a9e17911b11a498c3ee7a802bd82c7505.jpg)

![](images/f68dda4e8ed9136580701a90f5f643a27b823bcf0e39388baa6c0d776d7f4f0a.jpg)  
Figure 4. Intercalation and growth of h-CuI within twisted bilayer graphene. (a) $C _ { \mathcal { I } } / C _ { s ^ { - } }$ corrected HRTEM image (80 kV) of an h-CuI crystallite intercalated between two graphene layers after HI treatment at $40 \%$ . The inset FFT of the adjacent region reveals two hexagonal graphene lattices (G, G′) with a relative twist angle of $2 6 . 0 ^ { \circ } \pm 1 . 0 ^ { \circ }$ confirming the bilayer template. (b) FFT of the triple-layer heterostructure displaying reflections from both graphene layers (G, G′, white) and the intercalated h-CuI (red circles). (c) Structural schematic of the $40 ^ { \circ } \mathsf { C }$ configuration (Sample 3): $h { - } \mathsf { C u l }$ is sandwiched between G and $G ^ { \prime }$ with epitaxial twist angles $\theta = 1 4 . 4 ^ { \circ }$ and $\theta ^ { \prime } = 1 9 . 6 ^ { \circ }$ (defined as the deviation from $30 ^ { \circ }$ epitaxy, $\theta = | 3 0 ^ { \circ } - \Delta |$ , with $\Delta$ taken against the corresponding graphene layer; the raw lattice-vector angles $\Delta = 1 5 . 6 ^ { \circ }$ and $\Delta ^ { \prime } = 1 0 . 4 ^ { \circ }$ are listed in the SI), the two raw angles adding to $\Delta + \Delta ^ { \prime } = 2 6 . 0 ^ { \circ }$ and thus reproducing the $\sf { G } { - } \sf { G } ^ { \prime }$ twist of $2 6 . 0 ^ { \circ } \pm \dot { 1 } . 0 ^ { \circ }$ read directly from the FFT in panel (a). (d) HRTEM micrograph showing an expanded h-CuI domain within a bilayer region after thermal annealing at $1 8 0 ^ { \circ } \mathsf { C } .$ (e) Corresponding FFT showing $h { \mathrm { - } } \mathsf { C u l }$ reflections (red) in near-epitaxial alignment with one graphene layer $( \Theta ^ { \prime } \approx 0 ^ { \bar { \circ } }$ , locked to G′), while maintaining a twist angle of $\theta = 2 1 . 7 ^ { \circ }$ with the other layer (G). The overlapping reflection is the second-order h-CuI reflection, which nearly coincides with the first-order graphene spot by lattice commensurability. (f) Schematic reconstruction of the annealed h-CuI/BLG heterostructure based on experimental lattice vectors and orientation mapping.

with the other layer, G [Fig. 4(e)]. The obtained lattice parameters are $\mathsf { b } 1 = 0 . 4 1 9 \pm 0 . 0 0 2$ nm, $\mathsf { b } 2 = 0 . 4 2 2 \pm 0 . 0 0 2$ nm, and $\mathsf { b 3 } = 0 . 4 2 6 \pm 0 . 0 0 2$ nm. The anisotropy of 1.7% indicates the uniaxial strain profile, reflecting the lattice adaptation to the epitaxial template in only one direction, while h-CuI remains relaxed in the perpendicular direction, where $\mathfrak { b } 1 \ =$ $0 . 4 1 9 \pm 0 . 0 0 2$ nm is close to the intrinsic value. The simultaneous formation of h-CuI in monolayer and bilayer regions of the same substrate, under identical conditions, enables a direct comparison of the two configurations. In both, h-CuI grows epitaxially with a hexagonal lattice, which shows that intercalation into twisted bilayer graphene proceeds analogously to growth on the open monolayer surface. An additional crystal, which is located within the same bilayer flake and which also shares a grain boundary with the crystal of Fig. 4(d,e), is shown in Fig. S3. Yet it is locked to G instead of G′. A crystallite on an outer surface of bilayer graphene would be templated by the outermost sheet in both cases, so registry with different graphene layers would be impossible. Both crystals are shown together in one image in Fig. S2, identifying the h-CuI as encapsulated within two graphene sheets (Section S3).

## Stoichiometric and elemental analysis

To verify the chemical identity and spatial distribution of the synthesized crystals, we performed STEM-EDX analysis following the $1 8 0 ~ ^ { \circ } \mathsf { C }$ annealing step. High-angle annular dark-field (HAADF) imaging [Fig. 5(a)] — complemented by elemental mapping, see Supporting Information [Fig. S1] — reveals extended areas of h-CuI over several hundred nanometers on the graphene membrane. The magnified view [Fig. 5(b)] resolves these h-CuI islands at higher contrast, on both monolayer and few-layer graphene regions, further demonstrating that our vapor-phase route facilitates extensive growth on both open surfaces and within encapsulated environments.

The composite EDX elemental map [Fig. 5(c)] shows copper (Cu) and iodine (I) colocalized in the regions where crystals have formed, while the carbon (C) signal remains uniform across the graphene template. In the crystal-free region [region 1 in Fig. 5(c)] the Cu and I fractions fall to 0.38 and 0.05 at%, that is, 18 and 102 times below the crystalcovered region. Individual elemental maps are provided in Fig. S1 (Supporting Information). Quantitative EDX spectroscopy of the crystal-covered region [region 2 in Fig. 5(c); Fig. 5(d)] yields Cu and I atomic fractions of $7 . 0 0 \pm 1 . 0 7 \%$ and $5 . 1 0 \pm 0 . 6 7 \%$ . The resulting Cu:I ratio of $1 . 4 \pm 0 . 3$ is consistent with the 1:1 stoichiometry of copper(I) iodide within the accuracy of standardless EDX quantification. Part of the copper signal originates outside the crystals: the crystal-free region records 0.38 at% Cu. The bright, high-contrast particles in the HAADF images stem from residual gold contamination, located mainly on the holey-carbon support (Supporting Information, Section S1).

Thermal annealing significantly reduces the oxygen signal in the EDX maps (see Fig. S1e), indicating the effective removal of oxygen-containing functional groups and adsorbed water from the initial oxo-G template during the HI treatment and subsequent annealing. Sulfur (from the SDS surfactant) and sodium were not detected within the signal-to-noise limits of the current EDX acquisition. This suggests an efficient removal of SDS surfactant used during the DSA process to form the continuous oxo-G film. The absence of these elements confirms that the synthesis provides a clean graphene template for the formation of large-area h-CuI/graphene heterostructures. A weak Ca K line at 3.7 keV is also visible in the spectrum. It was not included in the quantification and is attributed to residues from the sample preparation.

## Growth mechanism and phase selection

Next, we discuss the possible growth mechanisms and the formation energies of the uniaxially strained h-CuI phase on SLG. An estimate of the formation energies indicates that h-CuI is metastable. The energetic penalty of the freestanding 2D phase relative to bulk γ-CuI [21] is estimated to be about 20.5 meV/Å² (see SI Section S4c). We performed DFT calculations to obtain $\mathsf { E } _ { \mathsf { v d W } }$ for the untwisted 3 × 3 h-CuI on $5 \times 5$ graphene supercell, see the supporting information Sections S4a–S4b. The van der Waals adhesion $\mathsf { E } _ { \mathsf { v d W } }$ of the heterostructure is 13.58 meV/Å<sup>2</sup> (0.218 J/m<sup>2</sup>) per graphene interface (SI Section S4c). This value is slightly lower than the vdW binding energy of 17.4 meV/Å<sup>2</sup> for the CuI–CuI interlayer. Thus, the h-CuI monolayer on SLG is energetically about 7.0 meV/Å<sup>2</sup> less favorable than γ-CuI. A graphene-encapsulated h-CuI monolayer would be more favorable than $\gamma \mathrm { - C u l }$ by 6.6 meV/Å<sup>2</sup>. The h-CuI monolayer on a graphene substrate is therefore metastable, while a second graphene interface would make it thermodynamically favored.

![](images/c3eac89e4076efb93d4dbd10815486e424160138b177d58813e47c80279e5fd1.jpg)  
(b)

![](images/054566a3a86381677f9a708371395af5721ac6cf1d33235b6fcd6cbd5ceb9b85.jpg)

![](images/cb2e66ff1f677b0a713a84ebe26ed0e83599b4a56a37ea2f86fa79adc79e490d.jpg)  
(d)

![](images/f122b2badfc875d1c3aaa669130a1dd13551355458c282d96742e2f51eaaa9b2.jpg)  
Figure 5. Elemental and stoichiometric characterization via STEM-EDX. (a) HAADF-STEM overview of the graphene flakes spanning the holey-carbon support, with extended areas of h-CuI; the bright particles are residual gold contamination (Supporting Information, Section S1). (b) Magnified view of the area in (a) at higher contrast, showing $h { - } \mathsf { C u l }$ domains (labeled) on both monolayer and few-layer graphene regions. (c) Composite EDX map of carbon (magenta), copper (blue), and iodine (green); Cu and I co-localize in the crystal-covered regions, whereas in the crystal-free region 1 both fall by one to two orders of magnitude. (d) Representative EDX spectrum acquired from the h-CuI domain labeled $" 2 "$ in (c), giving a Cu:I atomic ratio consistent with 1:1 within the quantification accuracy. Inset tables provide a comparative stoichiometric analysis of the crystal and the bare graphene substrate. The essential role of the Cu grid as the sole solidstate precursor was independently verified by a control experiment using an Au TEM grid, which yielded no h-CuI under otherwise identical conditions (see SI Section S1, Sample Preparation).

Its formation, however, is governed not only by thermodynamics but also by the available formation routes. First, the formation of γ-CuI would require a three-dimensional nucleus with dangling bonds. In classical nucleation theory the barrier for such a three-dimensional nucleus scales as $\Delta G ^ { \star }$ ∝ $\mathsf { v s u r f 3 } / \Delta \mu 2$ (γsurf the surface free energy, $\Delta \mu$ the chemicalpotential driving force). Under our conditions, the precursor elements arrive separately at a graphene interface. Iodine resides on the graphene surface after the HI treatment, and copper migrates in from the grid bars over a potential energy landscape flat enough to permit anomalous adatom diffusion at room temperature [32]. Thus, CuI forms in situ under dilute conditions, and the local supersaturation required to nucleate a threedimensional $\gamma \mathrm { - C u l }$ particle is unlikely to be reached. Furthermore, routes that yield γ-CuI nanosheets and epitaxial $\gamma \mathrm { - C u l }$ films sublime CuI powder from sources held at 360–450 $^ \circ \mathsf { C }$ [24,25]; in our process no component exceeds $1 8 0 ~ ^ { \circ } \mathsf { C } ,$ , far below appreciable CuI sublimation, so the molecular CuI flux that enables γ-phase growth is absent. Second, the h-CuI surface is self-saturating: its basal planes carry no dangling bonds, so the iodineterminated basal h-CuI plane cannot template γ-CuI. Moreover, the precursor species Cu and I are supplied on graphene and not on top of h-CuI, so a second layer cannot nucleate, which makes multilayer h-CuI (β-CuI) equally unlikely. Under these conditions where HI functions as both the reducing agent and the iodine source, the hexagonal phase does not have to be thermodynamically more favorable than $\gamma \mathrm { - C u l }$ . The conditions under which γ-CuI nucleates do not arise in the first place.

The observation of uniaxial strain in the extended h-CuI crystals (Samples 2, 4, and 5, and Ref. [26]) provides a constraint on the total energy balance for epitaxial growth of the 2D layer on graphene. To analyze this quantitatively, we employ a simple energy balance given by [33,34] (derivation in SI Section S4a)

$$
E _ {\text {total}} = - E _ {\text {vdW}} - \Delta U _ {P} f _ {\text {lock}} + F _ {\text {strain}},\tag{1}
$$

where $\mathsf { E } _ { \mathsf { v d W } }$ is the registry-independent van der Waals adhesion between h-CuI and graphene, ΔUP is the corrugation amplitude, the additional binding gained when the two lattices reach an energetically favorable, commensurate stacking, and flock ∈ [0, 1] is the lock-in factor (1 for biaxial commensurate registry, about 1/3 to 1/2 for uniaxial commensurate, 0 for the least favorable stacking; SI Section S4a). EvdW and ΔUP are defined as positive quantities, so that the two leading minus signs identify them as the stabilizing contributions. Fstrain, the elastic energy required to strain h-CuI toward commensurability, is positive and destabilizing; Etotal is referenced to the unstrained layer and the bare substrate (SI Section S4a). For complete commensurability, h-CuI would have to be stretched by the 1.7% lattice mismatch. In SI Section S4b we show that accommodating this biaxially would cost $\mathsf { F } _ { \mathsf { b i } } \approx 1 . 0 5 \ : \mathsf { m e V } / \mathsf { A } ^ { 2 }$ , whereas a uniaxial match costs only $\mathsf { F } _ { \mathsf { u n i } } \approx 0 . 3 0 \mathsf { m e V } / \mathsf { A } ^ { 2 }$ . The experimentally observed anisotropy of $1 . 4 - 1 . 7 \%$ over extended crystalline domains, see Table S1, shows that h-CuI adapts only uniaxially. The corrugation gain must therefore exceed the uniaxial cost but stay below the biaxial one, $0 . 3 0 < \Delta \mathsf { U } _ { \mathsf { P , e f f } } < 1 . 0 5 ~ \mathsf { m e V / A } ^ { 2 }$ . The lower bound inferred from the observed uniaxial strain exceeds the corrugation amplitudes reported from DFT calculations in the literature (≤ 0.14 meV/Å<sup>2</sup>, Table S3) [28] by about a factor of two, which we ascribe to the unavoidable simplification in the vdW potential assumed in those calculations.

Finally, we discuss how substrate defects and interfacial adsorbates affect the growth of h-CuI on graphene [29]. The balance of $\mathsf { E q . }$ (1) holds for an idealized interface. DFT calculations for a defective graphene substrate (Methods) give an adhesion of 13.65 meV/Å<sup>2</sup>, only 0.5% above the pristine value of 13.58 meV/Å<sup>2</sup>; the single defective configuration examined therefore leaves the balance of Eq. (1) unchanged. In contrast, interfacial adlayers have a pronounced effect on the epitaxial growth. We estimate their effect with a planar potential for two parallel sheets [39] (SI Section S4d),

$$
E _ {v d W} (z) = E _ {0} \left[ (5 / 3) (z _ {0} / z) ^ {4} - (2 / 3) (z _ {0} / z) ^ {1 0} \right],\tag{2}
$$

where $\textsf { Z }$ is the graphene–CuI distance, $z _ { 0 } = 3 . 6 8 \mathrm { ~ \AA ~ }$ is the equilibrium van der Waals gap (static DFT: 3.678 Å [26] and 3.675 Å [28]), and $\mathsf { E } _ { 0 }$ is the well depth, set to our calculated adhesion of $1 3 . 5 8 \mathrm { \ m e V } / \mathsf { A } ^ { 2 } ;$ the $z ^ { - 4 }$ attractive tail is the pairwise dispersion limit for two parallel sheets [39]. An adlayer that increases the interfacial distance by $\Delta z$ reduces the recovered adhesion to $\mathsf { E } _ { \mathsf { v d W } } ( \mathsf { Z } 0 \ + \ \Delta \mathsf { z } )$ The thickness of a single interfacial adlayer is comparable to the vdW gap itself: adsorbed water layers between graphene measure 3.7 $\pm 0 . 2 \mathsf { A }$ [40] and hydration layers in liquid water 2.8–3.0 Å [41]. Inserting $\Delta z = 2 . 8 – 3 . 7$ Å into Eq. (2) leaves a recovered adhesion of only 1.4–2.3 meV/Å<sup>2</sup>, that is 10–17% of E<sub>0</sub>, which cannot compensate the 20.5 meV/Å<sup>2</sup> by which the 2D phase lies above bulk γ-CuI. Because such an adlayer is an equilibrium feature of the open graphene surface in liquidphase synthesis, it offers an explanation for the absence of h-CuI on open monolayer regions in the wet-chemical route [26]. Within a bilayer, the van der Waals pressure expels part of the adsorbates into pockets [42,43] and presses the layers together, supporting the binding where adsorbates cannot be removed.

In our vapor-phase route the same balance appears in reverse: where adsorbates remain on the surface, the adhesion term of Eq. (1) is not recovered and growth stops. We compare two states of the interface, after HI treatment at $40 \%$ and after HI treatment followed by annealing at $1 8 0 ~ ^ { \circ } \mathsf { C }$ . After the $40 \%$ HI treatment the reduced oxo-graphene surface still carries residual oxo-groups, physisorbed water, and adsorbed iodine [35], limiting the size of the h-CuI crystallites. ${ \sf A t } 1 8 0 ^ { \circ } { \sf C } ,$ , coalesced domains form (Fig. 3; Fig. 5), and STEM-EDX records a cleaner interface, with the oxygen signal dropping and sulfur and sodium falling below the detection limit (Fig. S1). This correlation is consistent with a contribution from adsorbate removal; the adsorbates at this interface desorb or migrate with barriers reported for other systems that span roughly 0.01–0.9 eV: oxo-group hopping on graphene 0.15–0.89 eV [36], copper edge diffusion 0.17 eV [37], and adsorbed iodine 10–20 meV [38]. The lateral domain size therefore correlates with the local cleanliness of the interface, as seen in Fig. S2, where the h-CuI crystals extend up to the next adsorbate on the surface. Where the interface is clean, further growth is expected to be limited mainly by precursor supply to the graphene–CuI interface.

## Stability of h-CuI on graphene

In bulk, the layered hexagonal β-phase is an equilibrium phase only between 643 and 673 K and reverts to γ-CuI on cooling [16,21]. According to the observations, however, in two dimensions the phase persists to room temperature. Exfoliated flakes persist uncovered under ambient conditions [23]. Simulations find the freestanding lattice to be dynamically stable at room temperature [17,23]. A stabilizing effect of encapsulation in bilayer graphene was found in AIMD simulations, where the freestanding monolayer lost structural integrity at 600 K, while the encapsulated layer was still structurally stable [28]. Published calculations thus considered the freestanding monolayer [17,23] and the encapsulated layer [26,28] but not yet 2D h-CuI on an open graphene substrate, which is metastable by about 7.0 meV/Å<sup>2</sup> above bulk γ-CuI. To assess the stability of h-CuI also on SLG, we performed AIMD simulations at 300 and 600 K and compared the supported and encapsulated configurations. The cells used for the calculations were commensurate supercells with a typical twist angle of $\mathsf { \Omega } \otimes \approx 2 0 . 6 ^ { \circ }$ matching the annealed monolayer of Fig. 3(d), see SI Section S5. For each case at least six restart segments of about 1.5 ps were run, giving at least 9 ps of aggregate sampling per system (Section S5b).

We first analyze the collective movements within the h-CuI plane and relative to the additional graphene layers, Fig. 6(a)–(c). Panel (a) shows the power spectrum of the antisymmetric out-of-plane coordinate of the two CuI sublayers, $Z _ { \mathrm { a n t i } } = \mathrm { \Delta } ^ { 1 } / _ { 2 } ( \bar { z } _ { \mathrm { t o p } } - \mathrm { \Delta } \bar { z } _ { \mathrm { b o t } } )$ , at 300 K; see the inset of the figure for an illustration of the movement. Between 1.20 and 1.55 THz the oscillation in BLG-encapsulated and SLG-supported h-CuI shows a mean normalized power of $0 . 2 8 8 \pm \ : 0 . 0 7 4$ and $0 . 0 2 8 \pm \ : 0 . 0 2 2$ , respectively (Table S5). We attribute the damping to the strong spectral coherence $\mathsf { Y } ^ { 2 }$ between the out-of-plane centerof-mass motion of SLG and h-CuI, see Fig. 6(c). The curvature of the potential of Eq. (2) at its minimum defines a van der Waals spring normal to the plane [45,46], $\mathsf { k } = 4 0 \mathsf { E } _ { 0 } / \mathsf { z } _ { 0 } { } ^ { 2 } \approx$ 40 meV/Å<sup>4</sup>, or $6 . 4 \times 1 0 ^ { 1 9 } \mathsf { N } / \mathsf { m } ^ { 3 }$ . On single-layer graphene such a spring force is present on one side of h-CuI while it is present on both sides in BLG. The areal masses of the CuI sheet and of one graphene layer are 25.9 and 4.6 amu/Å<sup>2</sup>. Their reduced areal mass, $\mu =$ $( 2 5 . 9 \times 4 . 6 ) / ( 2 5 . 9 + 4 . 6 ) = 3 . 9$ in these units, places the layer-breathing mode of sheet against layer at $\mathsf { f } = ( 1 / 2 \pi ) \sqrt { ( \mathsf { k } / \mu ) } = 1 . 5 \theta$ THz, just above the observed band at 1.20–1.55 THz. The same adhesion well depth used in the preceding section therefore also sets the expected frequency scale of this collective out-of-plane motion. The coherence of h-CuI with SLG exceeds that with either graphene layer of BLG by a factor of 2.5 to 6. Averaged over the analyzed range, 0.9 to 3.0 THz, $\mathsf { Y } ^ { 2 }$ is $0 . 5 2 5 \pm 0 . 0 5 0$ on SLG, compared with 0.083 $\pm 0 . 1 3 4 $ and $0 . 2 0 6 \pm 0 . 1 7 6$ for the two graphene layers of BLG. Between 1.0 and 1.7 THz, $\mathsf { Y } ^ { 2 }$ is $0 . 6 5 6 \pm 0 . 0 6 7$ on SLG, and $0 . 1 0 1 \pm 0 . 3 1 7$ and $0 . 0 7 0 \pm 0 . 0 9 1$ for the two BLG layers.

For the case of h-CuI on SLG, the sheet and the graphene layer move together in a common layer-breathing mode. Thus, a single graphene layer damps the relative out-ofplane movement of h-CuI between 1.20 and 1.55 THz by an order of magnitude in normalized power. The band near 4 THz is the internal Cu–I bond vibration, which is

![](images/083d31eb7dc033f8f56b6443914d3680fc3fa4fe850582626d70ce921aee37a8.jpg)

![](images/235d054200e6d30696dbaee73ffdbf04c588b53543a643534e883e4f332a3803.jpg)

![](images/f134b5f1aa7708dcc959158ad9fed11ddf155942bf74570dd94b750c4804a68f.jpg)

![](images/b8bc2d4634dc1b8b78b510ec335925c83d34dbfdfb08be8d3fbacd6761b2ac60.jpg)

![](images/54b08bd0d31fae621a6b4324494f747cf4e7d5caf44c10ee73ac106c18a050a8.jpg)

![](images/a49d0ffa515190e2cdb58a1ca7e35151599bb51d03cb395c05e02e0c4c0f3b37.jpg)

![](images/42945ad4342519e0b0e520e9fa82d1a849665b1bfbbbef713a45eb0e871e789d.jpg)

![](images/d22ef204701ea09dcae34754d81e87c2ff6a47b6b05c49bf3e9b6a1c3153d133.jpg)

![](images/3da6c53358fb456565ae38b207f1ae2fb00bc7ed64ef465dccf603813ad47ef6.jpg)  
Figure 6. Ab initio molecular dynamics simulations of h-CuI on single-layer graphene and between two graphene layers. (a) Power spectrum of the antisymmetric out-of-plane coordinate of the two CuI sublayers, $\overline { { Z _ { \mathrm { a n t i } } } } = \frac { 1 } { / _ { 2 } } ( \bar { \ Z } _ { \mathrm { t o p } } - \bar { \ Z } _ { \mathrm { b o t } } )$ at 300 $\mathsf { K } ;$ each curve is normalized to its own maximum. (b) Power spectrum of the in-plane transverse optical coordinate ${ \sf T O } = \bar { \sf v } _ { \sf y } ( { \sf C u } ) - \bar { \sf v } _ { \sf y } ( { \sf I } )$ at 300 K (solid) and 600 K (dashed). (c) Squared spectral coherence $\mathsf { Y } ^ { 2 }$ between the out-of-plane center-of-mass motion of a graphene layer and that of the adjacent CuI sublayer at 300 K. The insets in (a)–(c) illustrate the analyzed dynamics for the example of SLG. (d, e) Pair distribution functions g(r) of iodine, (d), and of copper, (e), at 300 and 600 K. Markers indicate the typical distances of the hexagonal lattice with $\mathsf { a } = 4 . 1 \mathrm { ~ \AA ~ }$ $\sqrt { 3 a } = 7 . 1 \textrm { \AA }$ and $2 \mathsf { a } = 8 . 2 \mathsf { A }$ $\mathsf { a } ^ { \prime } = 4 . 5 \mathsf { A }$ appears in the iodine panel for the nearest neighbor in the other iodine sublayer. (f) In-plane mean-square displacement ${ \sf M S D } _ { \sf x y } ( { \sf T } )$ at 600 K. (g, h) Out-of-plane mean-square displacement ${ \sf M S D } _ { z } ( \tau )$ of iodine and of copper at 600 K, for the two sublayers (bottom and top). In SLG the bottom sublayer faces graphene, see the illustration in the insets of (a)–(c). (i) Plateau values of (g) and (h), averaged over $\mathsf { T } = 0 . 3 \mathrm { - } 1 . 0 ~ \mathsf { p s }$ . The asymmetry is highlighted by a bracket on top of the bar chart; b and t denote the bottom and the top sublayer.

similar for both cases, on SLG and on BLG. Fig. 6(b) shows the power spectrum of the inplane transverse optical coordinate, $\mathsf { T O } = \bar { \mathsf { v } } _ { \mathsf { y } } ( \mathsf { C u } ) - \bar { \mathsf { v } } _ { \mathsf { y } } ( \mathsf { I } )$ , of the movement of the copper sublattice relative to the iodine sublattice. At 300 K, the TO bands are found at $1 . 9 3 \pm 0 . 2 1$ and at $2 . 7 6 \pm 0 . 0 5$ THz for the SLG and BLG cases, respectively. For this collective inplane movement, a second interface stiffens the h-CuI sheet.

We then analyzed the pair distribution functions (PDF) g(r) of iodine with itself and of copper with itself inside the h-CuI to gain quantitative information on the structural stability. Fig. 6(d), (e) show the maxima at the characteristic distances of the double-hexagonal lattice with $\mathsf { a } = 4 . 1 2 \mathsf { A } ,$ , √3a = 7.14 Å and $2 \mathsf { a } = 8 . 2 4 \mathsf { A }$ , where a is the neighbor distance within one sublayer. For iodine an additional maximum appears at $\mathsf { a ^ { \prime } } = \mathsf { 4 . 4 9 }$ Å corresponding to the nearest neighbor in the second iodine sublayer of the $\mathsf { I } \mathsf { - C u \mathrm { - C u \mathrm { - } \mathsf { I } } }$ sandwich. The characteristic maxima in the distribution functions show that the hexagonal lattice is retained at 300 K both on SLG and within BLG. At 600 K the iodine atoms remain strongly localized, while the Cu atoms show increased dynamics. At the first minimum of the Cu–Cu distribution, at 5.69 Å, g(r) rises from 0.11 to 0.77 on SLG and from 0.15 to 0.71 in BLG. The hexagonal order is still maintained at 600 K, mainly by the iodine framework, while the copper sublattice may delocalize inside it. Fig. 6(f) confirms that the in-plane mean-square displacement MSDxy(τ) at 600 K for Cu is much higher. The iodine displacement reaches a plateau of 0.220 $\mathbb { A } ^ { 2 }$ , while the copper displacement keeps rising within the time frame of our simulation, see also Table S6. Over its longest continuous segment, 1.72 ps, a copper atom covers a mean net in-plane distance of 0.99 Å, a quarter of the neighbor distance. The copper therefore exhibits enhanced in-plane mobility within a framework maintained by the iodine sublattice. At 300 K, the movement of Cu within the I lattice is not observed; the $\mathsf { M S D } _ { \mathsf { x y } }$ of Cu reaches the iodine plateau and then remains constant.

Finally, we analyze the consequence of the different type of clamping of h-CuI on SLG and BLG, respectively. Fig. 6(g)–(h) show the out-of-plane mean-square displacement ${ \sf M S D } _ { \sf z } ( { \sf T } )$ of iodine and of copper at 600 K. Each is resolved by sublayer, after removing the center-of-mass motion of that sublayer. For a bound atom the plateau equals $2 \sigma _ { z } { } ^ { 2 }$ , so the amplitude follows as $\sigma _ { z } = \surd ( \mathsf { M S D } / 2 )$ On SLG, the bottom sublayer faces graphene and the top faces vacuum; in the encapsulated cell both faces are in contact with graphene. The two iodine sublayers behave differently on graphene, reaching 0.126 $\mathbb { A } ^ { 2 }$ for the bottom layer and 0.164 $\mathbb { A } ^ { 2 }$ for the top layer, see Fig. 6(g). With graphene on both faces the sublayers stabilize at a similar MSDz, 0.133 and 0.126 $\mathbb { A } ^ { 2 } .$ . The vdW spring of graphene thus damps the out-of-plane movement of the iodine sublayer in its vicinity. In BLG this damping is observed for both sublayers of $h \mathrm { - C u l ; }$ in SLG the damping is asymmetric and stronger on the sublayer in direct contact with graphene. In Fig. 6(i) we summarize the plateau values of (g) and (h), averaged over $\intercal = 0 . 3 – 1 . 0$ ps, with b and t for the bottom and the top sublayer. The effect on Cu is markedly smaller, which we attribute to the larger distance of Cu compared to I from the van der Waals interface with graphene. The trajectories show that 2D h-CuI remains dynamically stable not only within a graphene sandwich but also on an open graphene surface at both 300 and 600 K.

## CONCLUSIONS

We have demonstrated the bottom-up growth of two-dimensional hexagonal copper(I) iodide (h-CuI) directly on reduced oxo-graphene. HI-vapor treatment at $40 \%$ initiates $h \mathrm { - }$ CuI nucleation, while annealing at $1 8 0 ~ ^ { \circ } \mathsf { C }$ promotes the growth of extended crystalline domains on open monolayer graphene and within bilayer graphene. 80 kV Cc/Csaberration-corrected HRTEM resolves the atomic structure, local epitaxial alignment, and the characteristic uniaxial lattice anisotropy of the h-CuI domains, while STEM-EDX yields a Cu:I ratio consistent with 1:1. The lateral extent of the h-CuI domains correlates with the cleanliness of the interface and is limited mainly by remaining interfacial adsorbates.

DFT calculations give a van der Waals adhesion of 13.58 meV/Å² per graphene interface and identify h-CuI on open monolayer graphene as thermodynamically metastable, lying about 7.0 meV/Å² above bulk γ-CuI [21]. Under the present low-temperature precursor conditions, neither a molecular CuI vapor flux nor the local supersaturation required for γ- CuI nucleation is available, favoring selective formation of the hexagonal layer at the graphene interface. AIMD simulations further show that the hexagonal lattice remains intact at both 300 and 600 K on open monolayer graphene as well as within bilayer graphene. At 600 K, Cu atoms become increasingly mobile within an iodine framework that retains its hexagonal order.

The growth of oriented h-CuI on an open surface may be useful for its integration into heterostructure device platforms, combining the stability of graphene with the mechanical flexibility and favorable optoelectronic properties of the 2D metal halide. The predominantly van der Waals nature of the substrate interaction suggests that this approach is not restricted to graphene and h-CuI but may extend to other chemically inert 2D templates capable of stabilizing different metastable layered phases.

## EXPERIMENTAL METHODS

## Synthesis of h-CuI/r-oxo-G Heterostructures

Oxo-graphene (oxo-G) was synthesized using a modified Hummers method [47,48]. The oxo-G flakes were deposited onto standard copper TEM grids with an amorphous carbon support film (Quantifoil) by double self-assembly (DSA). In this process, oxo-G flakes selfassemble at the air–water interface and are compressed into a compact, non-overlapping film by sodium dodecyl sulfate (SDS) surfactant [49,50,52].

The oxo-G-coated copper grids were subsequently exposed to hydrogen iodide (HI) vapor to reduce the oxo-G template and initiate CuI formation. For this purpose, the samples were placed on a PTFE support inside a sealed reaction vessel containing 2 mL of aqueous HI solution (57 wt%). The reaction was carried out at $40 \%$ for 1 h. During this treatment, HI vapor acts both as a reducing agent for oxo-G, yielding reduced oxographene (r-oxo-G), and as an iodine source for CuI formation. The copper TEM grid serves as a sacrificial solid-state copper precursor. Under these conditions, CuI nucleates on the graphene flakes.

To promote the growth of extended h-CuI domains, the samples were subsequently annealed at $1 8 0 ~ ^ { \circ } \mathsf { C }$ for 2 h under ambient conditions. The essential role of the copper grid as the metal precursor was verified by control experiments using gold TEM grids, for which no h-CuI formation was observed under otherwise identical conditions. Further synthesis parameters and additional characterization are provided in the Supporting Information, Section S1.

## Materials Characterization

Atomic-scale structural characterization was performed using the chromatic- and spherical-aberration- $\mathrm { ( C _ { c } / C _ { s - } ) }$ corrected Sub-Angstrom Low-Voltage Electron Microscope (SALVE), operated at an accelerating voltage of 80 kV to minimize beam-induced damage. The instrument employs a combined $\mathtt { C c } / \mathtt { C s }$ corrector that compensates the thirdorder spherical aberration $\mathtt { C s }$ and the off-axial coma B3 together with the linear chromatic aberration, with residual geometric aberrations minimized up to fifth order [53]. Correcting $\mathtt { C s }$ removes the delocalization of lattice information, while the chromatic-aberration correction narrows the focus-spread envelope and thereby extends the information limit to 76 pm at 80 kV [53]. Measured values for $\mathtt { C c }$ and $\mathtt { C s }$ were in the range of −5 to −15 μm. The vacuum in the column of the TEM was ${ \sim } 2 { \cdot } 1 0 ^ { - 7 }$ mbar. Dose rates in the range of $1 0 ^ { 5 }$ $\mathsf { e } / ( \mathsf { n m } ^ { 2 } { \cdot } \mathsf { s } )$ were used for the high-resolution images, and the images were recorded on a $4 k \times 4 k$ CMOS camera with exposure times of 0.25–1 s. Chemical mapping and stoichiometric analysis were carried out by scanning transmission electron microscopy combined with energy-dispersive X-ray spectroscopy (STEM-EDX) using a Thermo Fisher Talos F200X operated at 80 kV and equipped with a high-sensitivity SuperX EDX detector.

The orientation and crystallinity of the h-CuI layers were analyzed from fast Fourier transforms (FFTs) of high-resolution TEM (HRTEM) images using the TemCompanion software suite [54]. Real-space h-CuI lattice vectors b1, ${ \mathsf { b } } _ { 2 } ,$ and b3 were determined by fitting two-dimensional Gaussian functions to the atomic columns in the HRTEM images using Atomap with HyperSpy [31], enabling high-precision determination of local lattice parameters. The graphene primitive vectors a1, a2, and a3 were extracted from the corresponding FFT reflections. All lattice measurements were internally calibrated against the graphene lattice constant a<sub>G</sub> = 2.460 Å, within the range of reported graphite basalplane values of 2.4589 Å [55] to 2.4617 Å [56], which removes the pixel-size uncertainty common to all vectors. Details of the atomic-column fitting procedure, lattice-vector analysis, and twist-angle determination are provided in the Supporting Information, Sections S2a–S2c and Tables S1 and S2.

## Ab initio Calculations and Molecular Dynamics Simulations

Static density functional theory (DFT) calculations of the interlayer binding between h-CuI and graphene were performed with the Vienna Ab initio Simulation Package (VASP) [57] within the projector augmented-wave (PAW) formalism [58]. The spin-polarized calculations used the Perdew-Burke-Ernzerhof (PBE) exchange–correlation functional [59], a plane-wave energy cut-off of 550 eV, and a Γ-centered Monkhorst–Pack k-point grid of $9 \times 9 \times 1$ . Dispersion was included through the DFT-D3 scheme [60] with Becke–

Johnson damping [61]. Structures were relaxed until all residual forces were below 0.01 eV $\mathsf { A } ^ { - 1 }$ , with an electronic convergence criterion of $1 0 ^ { - 6 } \in \mathsf { V }$

The supercell used for the binding energy contained 18 Cu, 18 I, and 50 C atoms, that is, a $3 \times 3 \ h { \mathrm { - } } { \mathsf { C u l } }$ cell on $5 \times 5$ graphene (rhombic cell of the hexagonal lattice, edge length 12.32 Å, area $\mathsf { A } = 1 3 1 . 4 \mathsf { A } ^ { 2 } )$ . In this cell the h-CuI in-plane lattice constant is 4.107 Å, 2.0% below the freestanding value of 4.19 Å, so the layer is compressed rather than stretched; the $( { \sqrt { 3 } } \times { \sqrt { 3 } } )$ commensuration discussed in the Vapor-phase growth on monolayer graphene section is a different registry. In this cell the $h { - } \mathsf { C u l }$ and the graphene hexagons are aligned, so the binding energies refer to the untwisted configuration and not to the twisted supercell of the molecular-dynamics runs described below. The binding energy was evaluated as $\mathsf { E } _ { \mathsf { b } } = \mathsf { E } ( \mathsf { G r } ) + \mathsf { E } ( h \mathrm { - } \mathsf { C u l } ) - \mathsf { E } ( h \mathrm { - } \mathsf { C u } | \ @ \mathsf { G r } )$ , the three terms being the total energies of the graphene sheet, of the h-CuI layer, and of the heterostructure; with this sign convention Eb is a positive adhesion energy. The adhesion energies quoted in the Growth mechanism and phase selection section, in the Stability of h-CuI on graphene section, and in the Supporting Information, Section S4c, are Eb divided by the area of one interface. The same protocol was applied to pristine single-layer graphene and to defective graphene.

Ab initio molecular dynamics (AIMD) simulations were performed with the CP2K package [62] in the Gaussian plane-wave (GPW) scheme [63], again with the PBE functional [59]. The valence electrons were expanded in double-ζ valence basis sets with one set of polarization functions (DZVP) from the molecularly optimized family [64], while the core electrons and the nuclei were described by Goedecker–Teter–Hutter (GTH) pseudopotentials [65]. Four multi-grids with a plane-wave cut-off of 400 Ry were used, the Brillouin zone was sampled at the Γ point only, the nuclear propagation time step was 0.5 fs, and trajectories were run at 300 and 600 K. The molecular-dynamics supercell was larger than the binding-energy cell and was twisted. Two heterostructure configurations were considered within one commensurate supercell defined by the parameters $\left| \mathsf { R } _ { 1 } \right| =$ $2 4 . 9 9 \mathring { \mathsf { A } } , | \mathsf { R } _ { 2 } | = 2 9 . 0 4 \mathring { \mathsf { A } } , \vee = 3 7 . 5 ^ { \circ }$ , area $\mathsf { A } _ { \mathsf { c e l l } } = 4 4 1 . 7 \mathsf { A } ^ { 2 }$ . The single-layer graphene (SLG) configuration consisted of one graphene layer and one h-CuI bilayer (60 Cu, 60 I, and 168 C atoms), whereas the bilayer graphene (BLG) configuration contained the same h-CuI bilayer encapsulated between two graphene layers (336 C atoms).

The integer commensurate matching, $\mathsf { R } _ { 1 } = ( 6 , 0 ) _ { h - \mathsf { C u l } }$ versus (9,2)Gr and ${ \sf R } _ { 2 } = ( 3 , 5 ) _ { h \mathrm { - } \mathsf { C u l } }$ versus $( 3 , 1 0 ) _ { \mathsf { G r } }$ , corresponds to a lattice-vector angle of $\Delta \approx 9 . 4 ^ { \circ }$ , i.e. an epitaxial twist of $\theta = | 3 0 ^ { \circ } - \Delta | \approx 2 0 . 6 ^ { \circ }$ (Section S2c and Fig. S4), close to the twist of the experimentally annealed monolayer sample $( \Theta = 2 1 . 2 ^ { \circ } \pm 1 . 0 ^ { \circ }$ , Table S2). This construction reproduces the lattice constant of freestanding graphene within 0.21% (a<sub>G</sub> = 2.464 Å compared with the reported range of 2.4589–2.4617 Å). In h-CuI, the mean in-plane lattice constant is 4.157 Å, corresponding to a bidirectional compressive strain of −0.79% relative to the freestanding value of 4.19 Å.

The supercell geometry, the spectral quantities read from Figure 6, the statistics of the restart segments, and the mean-square-displacement analysis of the Stability of h-CuI on graphene section are provided in the Supporting Information, Section S5.

## ASSOCIATED CONTENT

## Supporting Information

Additional details of the sample preparation, including double self-assembly deposition of oxo-graphene, hydrogen iodide vapor treatment, annealing, and the control synthesis on a gold grid; characterization methods, including determination of the h-CuI and graphene lattice vectors, twist-angle determination, and additional STEM-EDX data; additional bilayer graphene samples; energy balance calculation; analysis and methods description of the AIMD simulations; Figures S1–S5 and Tables S1–S7 (PDF)

## ACKNOWLEDGMENTS

D.K., A.T., G.J., J.P. and B.D.I. acknowledge the financial support from Thuringian Ministry of Economic Affairs, Science and Digital Society (TMWWDG) in Germany within the projects ESTI (2019 FGR 0080) and GraphSens (2020 FGR 0051) co-financed by the European Union (EU) within the European Social Fund (ESF). J.K., U.K., and A.N.K. acknowledge the funding of the Deutsche Forschungsgemeinschaft in the frame of the project DELAVER, funding Number 471707562. S.G. and E.B. acknowledge the financial support by the EPSRC Programme Grant 'Metal Atoms on Surfaces and Interfaces (MASI) for Sustainable Future' (EP/V000055/1). CPU time is provided by the ARCHER2 UK National Supercomputing Service, and the Sulis Tier 2 HPC platform funded by EPSRC Grant EP/T022108/1 and the HPC Midlands+ consortium. C.E.H. and S.E. gratefully acknowledge funding by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) through CRC 1772 (C01, project ID 555467911). We thank Michael Seifert from the Friedrich Schiller University Jena, Germany, for fruitful discussions. AIbased language tools were used to assist in editing and formatting the manuscript text; all scientific content, analyses, and conclusions were developed and verified by the authors, who take full responsibility for the published content.

## AUTHOR CONTRIBUTIONS

J.K. performed the HRTEM measurements, and J.K. and D.K. analyzed the HRTEM data. G.J. prepared the oxo-graphene deposition and performed the vapor-phase synthesis. S.G. performed the DFT and AIMD simulations, and D.K. and S.G. analyzed the simulation data. A.T. initiated and supervised the collaboration regarding the oxographene templates and sample preparation. C.E.H. and S.E. synthesized the oxographene material. B.D.-I. and J.P. supervised the h-CuI synthesis. E.B. supervised the first-principles calculations. A.K. contributed to the interpretation of the first-principles results and to the discussion. U.K. supervised the TEM studies and contributed to the discussion. A.T., B.D.-I., E.B., A.K. and U.K. acquired funding for the project. The manuscript was written by D.K., G.J., U.K., S.G., and E.B. with contributions of all coauthors.

## NOTES

The authors declare no competing financial interest.

## DATA AVAILABILITY

The data supporting the findings of this study are available from the corresponding author upon reasonable request.

## REFERENCES

[1] Shim, W.; Natelson, D.; Arbiol, J.; Besley, E.; et al. The Next 25 Years of Nanoscience and Nanotechnology: A Nano Letters Roadmap. Nano Lett. 2025, 25, 12789–12798.

[2] Kang, K. T.; Park, J.; Suh, D.; Choi, W. S. Synergetic Behavior in 2D Layered Material/Complex Oxide Heterostructures. Adv. Mater. 2019, 31, 1803732.

[3] Maggini, L.; Ferreira, R. R. 2D Material Hybrid Heterostructures: Achievements and Challenges Towards High Throughput Fabrication. J. Mater. Chem. C 2021, 9, 15721– 15734.

[4] Huang, P. Y.; Kurasch, S.; Alden, J. S.; et al. Imaging Atomic Rearrangements in Two-Dimensional Silica Glass: Watching Silica’s Dance. Science 2013, 342, 224–227.

[5] Iyengar, S. A.; Tripathi, M.; Srivastava, A.; et al. Glaphene: A Hybridization of 2D Silica Glass and Graphene. Adv. Mater. 2025, 37, 2419136.

[6] Manzeli, S.; Ovchinnikov, D.; Pasquier, D.; Yazyev, O. V.; Kis, A. 2D Transition Metal Dichalcogenides. Nat. Rev. Mater. 2017, 2, 17033.

[7] Gao, H.; Wang, Z.; Cao, J.; Lin, Y. C.; Ling, X. Advancing Nanoelectronics Applications: Progress in Non-van der Waals 2D Materials. ACS Nano 2024, 18, 16343–16358.

[8] Zhao, Y.; et al. Two-Dimensional Metals. Nature 2025, 639, 354–359.

[9] Al Balushi, Z. Y.; Wang, K.; Ghosh, R. K.; et al. Two-Dimensional Gallium Nitride Realized via Graphene Encapsulation. Nat. Mater. 2016, 15, 1166–1171.

[10] Krasheninnikov, A. V.; Lin, Y. C.; Suenaga, K. Graphene Bilayer as a Template for Manufacturing Novel Encapsulated 2D Materials. Nano Lett. 2024, 24, 12733–12740.

[11] Lehnert, T.; Kretschmer, S.; Brauer, F.; Krasheninnikov, A. V.; Kaiser, U. Quasi-Two-Dimensional NaCl Crystals Encapsulated between Graphene Sheets and their Decomposition under an Electron Beam. Nanoscale 2021, 13, 19626–19633.

[12] Lin, Y. C.; Motoyama, A.; Kretschmer, S.; et al. Polymorphic Phases of Metal Chlorides in the Confined 2D Space of Bilayer Graphene. Adv. Mater. 2021, 33, 2105898.

[13] Sinha, S.; Zhu, T.; France-Lanord, A.; et al. Atomic Structure and Defect Dynamics of Monolayer Lead Iodide Nanodisks with Epitaxial Alignment on Graphene. Nat. Commun. 2020, 11, 823.

[14] Algara-Siller, G.; Kurasch, S.; Sedighi, M.; Lehtinen, O.; Kaiser, U. The Pristine Atomic Structure of MoS2 Monolayer Protected from Electron Radiation Damage by Graphene. Appl. Phys. Lett. 2013, 103, 203107.

[15] Bädeker, K. Über die elektrische Leitfähigkeit und die thermoelektrische Kraft einiger Schwermetallverbindungen. Ann. Phys. 1907, 327, 749–766.

[16] Grundmann, M.; Schein, F.-L.; Lorenz, M.; Böntgen, T.; Lenzner, J.; von Wenckstern, H. Cuprous iodide — a p-type transparent semiconductor: history and novel applications, Phys. Status Solidi A 2013, 210, 1671–1703.

[17] Peng, B.; Li, Y.; Mu, L.; Chen, L. Two-Dimensional β-Phase Copper Iodide: A Promising Candidate for Low-Temperature Thermoelectric Applications. Sci. Rep. 2025, 15, 20535.

[18] Seifert, M.; Kawashima, M.; Rödl, C.; Botti, S. Layered CuI: a path to 2D p-type transparent conducting materials. J. Mater. Chem. C 2021, 9, 11284–11291.

[19] Ahn, J.; Yeon, E.; Hwang, D. K. Recent Progress in 2D Heterostructures for High-Performance Photodetectors and Their Applications. Adv. Optical Mater. 2025, 13, 2403412.

[20] Liu, A.; Zhu, H.; Park, W.-T.; Kang, S.-J.; Xu, Y.; Kim, M.-G.; Noh, Y.-Y. Roomtemperature solution-synthesized p-type copper(I) iodide semiconductors for transparent thin-film transistors and complementary electronics. Adv. Mater. 2018, 30, 1802379.

[21] Yang, W.; Wang, Y.; Yi, S.; et al. Structure of β-CuI: Stacking of 2D Bilayers. Chem. Mater. 2024, 36, 829–837.

[22] Mounet, N.; Gibertini, M.; Schwaller, P.; Campi, D.; Merkys, A.; Marrazzo, A.; Sohier, T.; Castelli, I. E.; Cepellotti, A.; Pizzi, G.; Marzari, N. Two-Dimensional Materials from High-Throughput Computational Exfoliation of Experimentally Known Compounds. Nat. Nanotechnol. 2018, 13, 246–252.

[23] Peng, B.; Jiang, J.; Wang, H.; et al. Ambiently Stable Two-Dimensional β-CuI Monolayers with Self-Trapping Exciton Luminescence. ACS Mater. Lett. 2025, 7, 1845– 1851.

[24] Yao, K.; Chen, P.; Zhang, Z.; Li, J.; Ai, R.; Ma, H.; Zhao, B.; Sun, G.; Wu, R.; Tang, X.; Li, B.; Hu, J.; Duan, X.; Duan, X. Synthesis of Ultrathin Two-Dimensional Nanosheets and Van der Waals Heterostructures from Non-Layered γ-CuI. npj 2D Mater. Appl. 2018, 2, 16.

[25] Gottschalch, V.; Benndorf, G.; Selle, S.; Krüger, E.; Blaurock, S.; Kneiß, M.; Bar, M.; Sturm, C.; Merker, S.; Höche, T.; Grundmann, M.; Krautscheid, H. Epitaxial Growth of Rhombohedral β- and Cubic γ-CuI. J. Cryst. Growth 2021, 570, 126218.

[26] Mustonen, K.; Hofer, C.; Kotrusz, P.; et al. Toward Exotic Layered Materials: 2D Cuprous Iodide. Adv. Mater. 2022, 34, 2106922.

[27] Peng, J.; Zhang, Q.; Zhang, Y.; et al. Unexpected Piezoresistive Effect, Room-Temperature Ferromagnetism, and Thermal Stability of 2D β-CuI Crystals in Reduced Graphene Oxide Membrane. Adv. Electron. Mater. 2023, 9, 2201241.

[28] Ullah, S.; Thonhauser, T.; Menezes, M. G. Optoelectronic Properties of Novel Layered Materials under Encapsulation: 2D Copper Iodide and Silver Iodide. Appl. Mater. Today 2024, 41, 102495.

[29] Krasheninnikov, A. V.; Batzill, M.; Delenda, A. A.; et al. Defects and Defect-Mediated Engineering of Two-Dimensional Materials: Challenges and Open Questions. Beilstein J. Nanotechnol. 2026, 17, 454–488.

[30] Konar, A.; Kaiser, D.; Jia, G.; Rasouli, H. R.; Köster, J.; Neumann, C.; Dellith, A.; Hübner, U.; Halbig, C. E.; Eigler, S.; Kaiser, U.; Dietzek-Ivanšić, B.; Plentz, J.; Turchanin, A. Highly Conductive and Transparent Coatings via Low-Temperature Hydroiodic Acid Vapor Treatment of Oxo-Graphene Thin Films. Adv. Mater. Technol. 2026, under revision (a copy is provided for review).

[31] Nord, M.; Vullum, P. E.; MacLaren, I.; Tybell, T.; Holmestad, R. Atomap: a new software tool for the automated analysis of atomic resolution images using twodimensional Gaussian fitting. Adv. Struct. Chem. Imaging 2017, 3, 9.

[32] Gervilla, V.; Zarshenas, M.; Sangiovanni, D. G.; Sarakinos, K. Anomalous versus Normal Room-Temperature Diffusion of Metal Adatoms on Graphene. J. Phys. Chem. Lett. 2020, 11, 8930–8936.

[33] Woods, C. R.; Britnell, L.; Eckmann, A.; et al. Commensurate–incommensurate transition in graphene on hexagonal boron nitride. Nat. Phys. 2014, 10, 451–456.

[34] Frank, F. C.; van der Merwe, J. H. One-Dimensional Dislocations. I. Static Theory. Proc. R. Soc. Lond. A 1949, 198, 205–216.

[35] Eigler, S.; Enzelberger-Heim, M.; Grimm, S.; Hofmann, P.; Kroener, W.; Geworski, A.; Dotzer, C.; Röckert, M.; Xiao, J.; Papp, C.; Lytken, O.; Steinrück, H.-P.; Müller, P.; Hirsch, A. Wet Chemical Synthesis of Graphene. Adv. Mater. 2013, 25, 3583–3587.

[36] Radovic, L. R.; Suarez, A. M.; Vallejos-Burgos, F.; Sofo, J. O. Oxygen migration on the graphene surface. 2. Thermochemistry of basal-plane diffusion (hopping). Carbon 2011, 49, 4226–4238.

[37] Zhao, Y.; Liu, Z.; Sun, T.; Zhang, L.; Jie, W.; Wang, X.; Xie, Y.; Tsang, Y. H.; Long, H.; Chai, Y. Mass Transport Mechanism of Cu Species at the Metal/Dielectric Interfaces with a Graphene Barrier. ACS Nano 2014, 8, 12601–12611.

[38] Jaiswal, N. K.; Patel, C. Density functional insights of iodine interaction with graphene and its nanoribbon with zigzag edges. Physica B 2018, 545, 268–274.

[39] Gould, T.; Gray, E.; Dobson, J. F. Van der Waals dispersion power laws for cleavage, exfoliation, and stretching in multiscale, layered systems. Phys. Rev. B 2009, 79, 113402.

[40] Xu, K.; Cao, P.; Heath, J. R. Graphene Visualizes the First Water Adlayers on Mica at Ambient Conditions. Science 2010, 329, 1188–1191.

[41] Garcia, R. Interfacial Liquid Water on Graphite, Graphene, and 2D Materials. ACS Nano 2023, 17, 51–69.

[42] Kretinin, A. V.; Cao, Y.; Tu, J. S.; et al. Electronic Properties of Graphene Heterostructures with Different Two-Dimensional Atomic Crystals. Nano Lett. 2014, 14, 3270–3276.

[43] Khestanova, E.; Guinea, F.; Fumagalli, L.; Geim, A. K.; Grigorieva, I. V. Universal Shape and Pressure inside Bubbles Appearing in van der Waals Heterostructures. Nat. Commun. 2016, 7, 12587.

[44] Lee, C.; Wei, X.; Kysar, J. W.; Hone, J. Measurement of the Elastic Properties and Intrinsic Strength of Monolayer Graphene. Science 2008, 321, 385–388.

[45] Kumar, H.; Er, D.; Dong, L.; Li, J.; Shenoy, V. B. Elastic Deformations in 2D van der Waals Heterostructures and their Impact on Optoelectronic Properties. Sci. Rep. 2015, 5, 10872.

[46] Le, N. B.; Huan, T. D.; Woods, L. M. Interlayer Interactions in van der Waals Heterostructures: Electron and Phonon Properties. ACS Appl. Mater. Interfaces 2016, 8, 6286–6292.

[47] Eigler, S. Controlled Chemistry Approach to the Oxo-Functionalization of Graphene. Chem. Eur. J. 2016, 22, 7012–7027.

[48] Eigler, S.; Hirsch, A. Chemistry with Graphene and Graphene Oxide—Challenges for Synthetic Chemists. Angew. Chem. Int. Ed. 2014, 53, 7720–7738.

[49] Jia, G.; Plentz, J.; Presselt, M.; et al. A Double Self-Assembly Process for Versatile Reduced-Graphene-Oxide Layer Deposition and Conformal Coating on 3D Structures. Adv. Mater. Interfaces 2017, 4, 1700758.

[50] Jia, G.; Plentz, J.; Kawamoto, N.; et al. A Novel Approach for the Preparation of Graphene Coatings by the Self-Assembly Technique. Coatings 2019, 9, 138.

[51] Murillo, M.; García-Hernan, A.; López, J.; Perles, J.; Brito, I.; Amo-Ochoa, P. The Flexibility of CuI Chains and the Functionality of Pyrazine-2-Thiocarboxamide Keys to Obtaining New Cu(I)–I Coordination Polymers with Potential Use as Photocatalysts for Organic Dye Degradation. Catal. Today 2023, 418, 114072.

[52] Jia, G.; et al. Graphene Oxide Membranes for Gas Separation. J. Membr. Sci. 2025, 717, 123617.

[53] Linck, M.; Hartel, P.; Uhlemann, S.; et al. Chromatic Aberration Correction for Atomic Resolution TEM Imaging from 20 to 80 kV. Phys. Rev. Lett. 2016, 117, 076101.

[54] Ma, T. TemCompanion: An Open-Source Multi-Platform GUI Program for TEM Image Processing and Analysis. SoftwareX 2025, 31, 102212.

[55] Baskin, Y.; Meyer, L. Lattice Constants of Graphite at Low Temperatures. Phys. Rev. 1955, 100 (2), 544. https://doi.org/10.1103/PhysRev.100.544.

[56] Howe, J. Y.; Rawn, C. J.; Jones, L. E. Improved Crystallographic Data for Graphite. Powder Diffr. 2003, 18 (2), 150–154. https://doi.org/10.1154/1.1536926.

[57] Kresse, G.; Furthmüller, J. Efficient Iterative Schemes for Ab Initio Total-Energy Calculations Using a Plane-Wave Basis Set. Phys. Rev. B 1996, 54, 11169–11186.

[58] Kresse, G.; Joubert, D. From Ultrasoft Pseudopotentials to the Projector Augmented-Wave Method. Phys. Rev. B 1999, 59, 1758–1775.

[59] Perdew, J. P.; Burke, K.; Ernzerhof, M. Generalized Gradient Approximation Made Simple. Phys. Rev. Lett. 1996, 77, 3865–3868.

[60] Grimme, S.; Antony, J.; Ehrlich, S.; Krieg, H. A Consistent and Accurate Ab Initio Parametrization of Density Functional Dispersion Correction (DFT-D) for the 94 Elements H–Pu. J. Chem. Phys. 2010, 132, 154104.

[61] Grimme, S.; Ehrlich, S.; Goerigk, L. Effect of the Damping Function in Dispersion Corrected Density Functional Theory. J. Comput. Chem. 2011, 32, 1456–1465.

[62] Kühne, T. D.; Iannuzzi, M.; Del Ben, M.; Rybkin, V. V.; Seewald, P.; Stein, F.; Laino, T.; Khaliullin, R. Z.; Schütt, O.; Schiffmann, F.; et al. CP2K: An Electronic Structure and Molecular Dynamics Software Package – Quickstep: Efficient and Accurate Electronic Structure Calculations. J. Chem. Phys. 2020, 152, 194103.

[63] VandeVondele, J.; Krack, M.; Mohamed, F.; Parrinello, M.; Chassaing, T.; Hutter, J. Quickstep: Fast and Accurate Density Functional Calculations Using a Mixed Gaussian and Plane Waves Approach. Comput. Phys. Commun. 2005, 167, 103–128.

[64] VandeVondele, J.; Hutter, J. Gaussian Basis Sets for Accurate Calculations on Molecular Systems in Gas and Condensed Phases. J. Chem. Phys. 2007, 127, 114105.

[65] Goedecker, S.; Teter, M.; Hutter, J. Separable Dual-Space Gaussian Pseudopotentials. Phys. Rev. B 1996, 54, 1703–1710.

# Supporting Information

## S1. Sample Preparation

The synthesis of nanohybrid heterostructures of h-CuI on reduced oxo-graphene [S1] follows the steps (A)–(F) listed below. In brief, oxo-graphene (oxo-G) [S2] is deposited directly onto a copper TEM grid with an amorphous carbon support film (Quantifoil) using the Double Self-Assembly (DSA) method [S3]. Subsequently, the sample is exposed to hydrogen iodide (HI) vapor. This treatment reduces the oxo-G and simultaneously initiates the nucleation of small h-CuI crystallites, formed from iodine supplied by the reducing agent and copper provided by the TEM grid. Finally, the sample undergoes thermal annealing at 180 °C, which promotes the reaction between iodine and copper to form extended, welldefined h-CuI crystals on the reduced oxo-G (r-oxo-G) substrate or sandwiched between the graphene nanosheets of bilayer r-oxo-G.

A) Materials and Substrate Preparation: A suspension of oxo-G flakes in a 1:1 volume ratio of deionized water and isopropanol was used as the initial material. Standard copper TEM grids (Quantifoil with amorphous carbon support) were used as substrates. Prior to deposition, the TEM grids and the petri dishes used for the assembly were thoroughly cleaned. They were placed in an ultrasonic bath with acetone for 15 minutes, followed by multiple rinses with high-purity water (18.2 MΩ·cm), and finally blow-dried with nitrogen gas.

B) Film Assembly at the Air-Water Interface: The cleaned petri dish was filled with ultrapure water. The oxo-G suspension, which was homogenized for 30 minutes in an ultrasonic bath, was then carefully dispensed onto the water’s surface using a syringe until the entire surface was covered with a loosely arranged, floating layer of oxo-G flakes.

C) Film Compression: To compress this layer, a 10% aqueous solution of sodium dodecyl sulfate (SDS) was introduced dropwise from a separate syringe at the edge of the petri dish. The SDS molecules rapidly spread across the water’s surface, acting as a mobile barrier that pushed the floating oxo-G flakes to the opposite side of the dish. This process caused the flakes to form a stable, compact, and uniform monolayer film. The compression was analogous to the Langmuir–Blodgett process, with the difference that the SDS molecules rearranged by self-assembly, so that a compact, uniform monolayer was maintained throughout the deposition.

D) Transfer onto TEM Grids: The liquid was carefully drained from the petri dish, leaving the compact oxo-G film floating on a thin layer of residual water. The film was then captured by carefully bringing the TEM grid up from underneath the film, allowing the film to settle and adhere to the grid’s surface. Finally, the grid with the deposited film was heated in an oven at $80 \%$ for 15 minutes to ensure it was thoroughly dried before subsequent synthesis steps.

E) HI-Vapor Treatment of oxo-G Films: The HI-vapor treatment was performed in a sealed glass container equipped with a Teflon sample support. First, 2 ml of an aqueous hydrogen iodide solution (57 wt%) was placed at the bottom of the container. The oxo-graphenecoated TEM grid was then positioned on the Teflon support, ensuring it was suspended above the liquid and not in direct contact with it. The container was sealed and placed in a furnace, where it was heated to $40 \%$ for one hour.

F) Annealing: Following the HI treatment, the samples were annealed in a separate furnace at $1 8 0 ^ { \circ } \mathrm { C }$ for two hours under ambient conditions.

To verify that the copper TEM grid serves as the essential copper source for h-CuI formation, an identical synthesis was performed using a gold $( \mathsf { A u } )$ TEM grid instead. The oxo-G film was deposited onto the Au grid following the same DSA protocol, subjected to the same HI vapor treatment at $40 ~ ^ { \circ } \mathsf { C }$ for one hour, and annealed at $1 8 0 ~ ^ { \circ } \mathrm { C }$ for two hours. Under these conditions, no h-CuI crystals were observed. The absence of h-CuI formation on the Au grid confirms that the copper from the Cu TEM grid is the sole source of Cu atoms in our synthesis, validating the solid-state precursor approach. In HAADF-STEM images of HItreated and annealed samples, bright high-contrast particles are observed mainly on the holey-carbon support; EDX identifies them as residual gold contamination.

## S2. Characterization Methods

Scanning transmission electron microscopy (STEM) and energy-dispersive X-ray spectroscopy (EDX) were performed on a Thermo Fisher Talos F200X (S)TEM operated at an acceleration voltage of 80 kV. High-resolution atomic structure imaging was conducted using the $\mathsf { C } _ { \mathsf { c } } / \mathsf { C } _ { \mathsf { s } ^ { - } }$ -corrected “Sub-Angstrom Low-Voltage Electron Microscope” (SALVE) instrument at 80 kV [S4].

## S2a. h-CuI Lattice Vectors

High-resolution TEM images were analyzed using Atomap with HyperSpy [S5]. Atomic column positions were identified using peak finding and refined by fitting 2D Gaussian functions to each atomic column, achieving a precision of \~1 pm. The 2D Gaussian fit provides the position $( \mathsf { x } , \mathsf { y } )$ , amplitude, and shape parameters $( \sigma _ { \mathrm { x } } , \sigma _ { \mathrm { y } } ,$ rotation angle) for each atomic column. From the detected atom positions, three principal lattice directions $( \mathbf { b } _ { 1 } , \mathbf { b } _ { 2 } )$ $\left| \mathsf { b } _ { 3 } \right.$ are automatically identified, corresponding to the three symmetry-equivalent translation directions of the hexagonal lattice, each separated by ${ \sim } 6 0 ^ { \circ } ;$ ; for Table S1 they are relabeled in ascending order of length. The graphene lattice constant $( \mathsf { a } _ { \mathsf { G } } = 2 . 4 6 0 \ \mathring { \mathsf { A } } = 0 . 2 4 6 0$ nm; Methods of the main text) served as internal calibration for the nm/pixel in the HRTEM image.

## S2b. Graphene Lattice Vectors

FFT performed using TemCompanion software [S6] was used to determine the angle of the graphene lattice vectors. The same internal calibration $\left( \mathsf { a } _ { \mathsf { G } } \right)$ as in S2a was applied.

## S2c. Twist Angle Determination

The epitaxial twist angle $\theta = | 3 0 ^ { \circ } - \Delta |$ quantifies the deviation from perfect $30 ^ { \circ }$ alignment between $h { - } \mathsf { C u l }$ and graphene, where Δ is the angular difference between the nearest h-CuI and graphene lattice vectors (Table S2).

The direct-FFT inter-graphene twist $\Phi _ { ^ { \mathsf { G G } ^ { \prime } } } = 2 1 . 7 \pm 1 . 0 ^ { \circ }$ is reported for the annealed bilayer crystallites that align to a single graphene layer, Sample 4 in Fig. 4(d–f) $( h { - } \mathsf { C u l }$ aligned with G′) and Sample 5 in Fig. S3 (aligned with G). The $\yen 123$ uncertainty reflects that the inter-layer twist cannot be read from the diffraction spots to better than about one degree. For these two samples the h-CuI lattice is aligned with one graphene layer at the commensurate $30 ^ { \circ }$ orientation, so the entries for that layer are quoted as idealized values $( \Delta ^ { \prime } \approx 3 0 ^ { \circ }$ and $\Theta ^ { \prime } \approx 0 ^ { \circ }$ for Sample $4 ; \theta \approx 0 ^ { \circ }$ for Sample 5). The angles to the other layer follow from the intergraphene twist as $\Delta = 8 . 3 ^ { \circ }$ (Sample 4) and $\Delta ^ { \prime } = 8 . 3 ^ { \circ }$ (Sample 5), i.e. $3 0 ^ { \circ } - 2 1 . 7 ^ { \circ }$ , with $\theta = \theta ^ { \prime } =$ $2 1 . 7 \%$ ; these values are average values of the vectors calculated from atomap, $7 . 7 ^ { \circ }$ and 9.1°, for the two samples.

Table S1. Lattice vectors for h-CuI/graphene heterostructures. Samples 1–2 = monolayer graphene (SLG); Samples 3–5 = bilayer graphene (BLG). $\mathsf { a } _ { 1 } , \mathsf { a } _ { 2 } , \mathsf { a } _ { 3 } = \mathsf { g r a p h e n e }$ (G) lattice vectors from $\mathsf { F F T } ; \mathsf { a } _ { 1 } ^ { \prime } ,$ $\hat { \mathbf { a } } _ { 2 } ^ { \prime } , \hat { \mathbf { a } } _ { 3 } ^ { \prime } =$ lattice vectors of the second graphene layer (G′); b<sub>1</sub>, b<sub>2</sub>, $\mathsf { b } _ { 3 } = \mathsf { h } \mathsf { - C u } \mathsf { I }$ lattice vectors from Atomap; $\mathsf { A } _ { \mathsf { b } } = \mathsf { a n i s o t r o p y }$ ${ \mathsf { T } } { = } 4 0 { \mathsf { \circ } } { \mathsf { C } } { \mathrm { : } }$ HI vapor treatment at $40 \%$ only, $\mathsf { T } { = } 4 0 / 1 8 0 ^ { \circ } \mathsf { C } ;$ HI vapor treatment at $40 \%$ followed by thermal annealing at $1 8 0 ~ { } ^ { \circ } \mathrm { C }$ . The h-CuI vectors are labeled in ascending order of length; their magnitudes are computed from the unrounded components. The graphene lattice constant $\mathtt { a } _ { \mathtt { G } } = 0 . 2 4 6 0$ nm serves as internal calibration (Section S2a), |a|=0.246 nm for all graphene lattice vectors.

<table><tr><td>Sample</td><td>Substrate / Growth temperature</td><td>Graphene Lattice vectors</td><td>h-Cul Lattice vectors</td></tr><tr><td rowspan="4">1(see Fig. 3)</td><td rowspan="4">r-oxo-G monolayer / 40 °C</td><td rowspan="4"> $a_1=(0.108, -0.221) \text{ nm}$  $a_2=(0.138, 0.204) \text{ nm}$  $a_3=(0.245, -0.017) \text{ nm}$ </td><td> $b_1=(0.060, -0.425) \text{ nm}$  $|b_1|=0.429 \pm 0.002 \text{ nm}$ </td></tr><tr><td> $b_2=(0.400, -0.162) \text{ nm}$  $|b_2|=0.431 \pm 0.002 \text{ nm}$ </td></tr><tr><td> $b_3=(-0.340, -0.264) \text{ nm}$  $|b_3|=0.431 \pm 0.002 \text{ nm}$ </td></tr><tr><td> $A_b=1.005 \pm 0.004$ </td></tr><tr><td rowspan="4">2(see Fig. 3)</td><td rowspan="4">r-oxo-G monolayer / 40 °C/180 °C</td><td rowspan="4"> $a_1=(0.170, 0.178) \text{ nm}$  $a_2=(0.239, -0.058) \text{ nm}$  $a_3=(-0.069, 0.236) \text{ nm}$ </td><td> $b_1=(0.056, -0.418) \text{ nm}$  $|b_1|=0.421 \pm 0.002 \text{ nm}$ </td></tr><tr><td> $b_2=(0.395, -0.158) \text{ nm}$  $|b_2|=0.425 \pm 0.002 \text{ nm}$ </td></tr><tr><td> $b_3=(-0.339, -0.260) \text{ nm}$  $|b_3|=0.427 \pm 0.002 \text{ nm}$ </td></tr><tr><td> $A_b=1.014 \pm 0.004$ </td></tr><tr><td rowspan="4">3(see Fig. 4)</td><td rowspan="4">r-oxo-G bilayer / 40 °C</td><td rowspan="4"> $a_1=(-0.003, 0.246) \text{ nm}$  $a_2=(0.214, -0.121) \text{ nm}$  $a_3=(0.212, 0.125) \text{ nm}$  $a_1'=(0.110, -0.220) \text{ nm}$  $a_2'=(0.246, -0.015) \text{ nm}$  $a_3'=(0.136, 0.205) \text{ nm}$ </td><td> $b_1=(-0.291, -0.298) \text{ nm}$  $|b_1|=0.416 \pm 0.002 \text{ nm}$ </td></tr><tr><td> $b_2=(0.116, -0.399) \text{ nm}$  $|b_2|=0.416 \pm 0.002 \text{ nm}$ </td></tr><tr><td> $b_3=(0.407, -0.101) \text{ nm}$  $|b_3|=0.419 \pm 0.002 \text{ nm}$ </td></tr><tr><td> $A_b=1.007 \pm 0.004$ </td></tr><tr><td rowspan="4">4(see Fig. 4)</td><td rowspan="4">r-oxo-G bilayer / 40 °C /180 °C</td><td rowspan="4"> $a_1=(0.057, -0.239) \text{ nm}$  $a_2=(0.236, -0.070) \text{ nm}$  $a_3=(-0.178, -0.169) \text{ nm}$  $a_1'=(0.245, -0.026) \text{ nm}$  $a_2'=(0.145, -0.199) \text{ nm}$  $a_3'=(0.100, -0.225) \text{ nm}$ </td><td> $b_1=(0.041, -0.417) \text{ nm}$  $|b_1|=0.419 \pm 0.002 \text{ nm}$ </td></tr><tr><td> $b_2=(0.387, -0.168) \text{ nm}$  $|b_2|=0.422 \pm 0.002 \text{ nm}$ </td></tr><tr><td> $b_3=(-0.345, -0.249) \text{ nm}$  $|b_3|=0.426 \pm 0.002 \text{ nm}$ </td></tr><tr><td> $A_b=1.017 \pm 0.004$ </td></tr><tr><td rowspan="4">5 (see Fig. S3)</td><td rowspan="4">r-oxo-G bilayer / 40 °C /180 °C</td><td rowspan="4"> $a_1=(0.178, 0.169) \text{ nm}$  $a_2=(0.057, -0.239) \text{ nm}$  $a_3=(0.236, -0.070) \text{ nm}$  $a_1'=(0.145, -0.199) \text{ nm}$  $a_2'=(0.100, 0.225) \text{ nm}$  $a_3'=(0.245, 0.026) \text{ nm}$ </td><td> $b_1=(0.297, -0.294) \text{ nm}$  $|b_1|=0.418 \pm 0.002 \text{ nm}$ </td></tr><tr><td> $b_2=(-0.114, -0.405) \text{ nm}$  $|b_2|=0.421 \pm 0.002 \text{ nm}$ </td></tr><tr><td> $b_3=(0.411, 0.111) \text{ nm}$  $|b_3|=0.426 \pm 0.002 \text{ nm}$ </td></tr><tr><td> $A_b=1.019 \pm 0.004$ </td></tr></table>

<table><tr><td>Sample</td><td> $b_3$ (°)</td><td>a (°)</td><td> $\Delta$ (°)</td><td> $\theta$ (°)</td><td> $\Delta'$ (°)</td><td> $\theta'$ (°)</td></tr><tr><td>1</td><td>37.8 ± 1.0</td><td>55.9 ± 1</td><td>18.1 ± 1.0</td><td>11.9 ± 1.0</td><td>—</td><td>—</td></tr><tr><td>2</td><td>37.5 ± 1.0</td><td>46.3 ± 1</td><td>8.8 ± 1.0</td><td>21.2 ± 1.0</td><td>—</td><td>—</td></tr><tr><td>3</td><td>-13.9 ± 1.0</td><td>-29.5 ± 1</td><td>15.6 ± 1.0</td><td>14.4 ± 1.0</td><td>10.4 ± 1.0</td><td>19.6 ± 1.0</td></tr><tr><td>4</td><td>35.8 ± 1.0</td><td>43.5 ± 1</td><td>8.3 ± 1.0</td><td>21.7 ± 1.0</td><td>≈30</td><td>≈0</td></tr><tr><td>5</td><td>15.1 ± 1.0</td><td>43.5 ± 1</td><td>28.4 ± 1.0</td><td>≈0</td><td>8.3 ± 1.0</td><td>21.7 ± 1.0</td></tr></table>

Table S2. Epitaxial twist angle calculation. b<sub>3</sub> = orientation of the h-CuI lattice vector ${ \sf b } _ { 3 }$ (Table S1); a = nearest graphene (G) lattice vector orientation; Δ = angle between lattice vector of graphene layer G and h-CuI; $\Delta ^ { \prime } = \mathsf { a n g l e }$ between lattice vector of graphene layer $\boldsymbol { \mathsf { G } ^ { \prime } }$ and h-CuI; $\theta = | 3 0 ^ { \circ } - \Delta |$ = deviation from ${ 3 0 ^ { \circ } }$ perfect lock-in. Orientations are given modulo 180°.

Fig. S1 presents the individual EDX elemental maps of the composite map shown in Fig. 5 of the main text.  
![](images/0c0986c3193ee299fdf98df2be5e961fc3d74de1a78e7ecfe012f2e7939b07da.jpg)  
Figure S1. Individual EDX elemental maps corresponding to the STEM-EDX analysis in Fig. 5 of the main text. (a) Composite EDX map showing the spatial distribution of all detected elements. (b) Carbon EDX map (C-K). (c) Copper EDX map (Cu-L). (d) Iodine EDX map (I-L). (e) Oxygen EDX map (O-K), showing reduced oxygen content in the crystal regions after annealing.

## S3. Additional Bilayer Graphene Samples

Fig. S2 resolves individual h-CuI crystallites at atomic resolution after annealing. Two adjacent domains, false-colored cyan and magenta, each show the continuous hexagonal h-CuI lattice, while the surrounding graphene is contaminated. The lateral domain sizes are about 20 and 27 nm. The domains terminate where they meet these contaminated regions, consistent with the contamination-limited growth identified in the Formation Mechanism and Stability section of the main text. The two domains are the crystallites analysed in Fig. 4(d–f) (Sample 4) and in Fig. S3 (Sample 5); the panels of both figures are taken from this field of view. Where they meet, they abut along a common boundary without overlapping, so both grew in the same plane.

![](images/09b515ff39f729d74d51782c8509de1af72191344628fb90abee944f654f15f2.jpg)  
Figure S2. Atomic-resolution HRTEM of h-CuI crystallites within reduced oxo-graphene bilayer after annealing. Two adjacent crystalline domains (false-colored cyan and magenta), with lateral sizes of about 20 and 27 nm against the 5 nm scale bar (within the up to about 30 nm range reported in the main text), terminate at the surrounding amorphous, contaminated regions.

Both crystallites are located within the same bilayer flake: Table S1 lists the same six graphene lattice vectors for Sample 4 and for Sample 5, so G and $\zeta ^ { \prime }$ denote the same two sheets in both cases. Sample 4 is nevertheless locked at the commensurate $30 ^ { \circ }$ orientation to $\boldsymbol { \mathsf { G } ^ { \prime } }$ and Sample 5 to G, each keeping $2 1 . 7 \pm 1 . 0 ^ { \circ }$ to the respective other sheet (Table S2), and Fig. S2 shows the two domains meeting in one plane. A crystallite adsorbed on the outer surface would be templated by the outermost sheet, which is the same sheet for both domains. Registry with different sheets from within one plane is available only in the gallery, which places the bilayer crystallites between the graphene layers.

Fig. S3 shows the additional h-CuI crystal within bilayer graphene after annealing (Sample 5 in Table S1). The FFT inset in panel (a) confirms the bilayer substrate through the presence of two rotated graphene lattices (G, G′). The FFT of the heterostructure region [Fig. S3(b)] reveals that the h-CuI diffraction spots (red dashed hexagon) nearly overlap with those of G, indicating $\theta \approx 0 ^ { \circ }$ (Table S2). The crystal therefore adopts epitaxial alignment with G rather than with the second graphene layer G′. The structure model [Fig. S3(c)], reconstructed from the experimental lattice vectors and orientation mapping as in Figs. 3 and 4, shows this reversed alignment configuration in top and side view. This crystal complements the bilayer sample documented in Fig. 4 of the main text. Together they show that h-CuI can adopt either graphene layer as its epitaxial template.

# S4. Energy Balance for h-CuI Growth on Graphene

## S4a. Model

The moiré total-energy density of a 2D layer on a misoriented substrate reads (Woods 2014 [S7], based on the Frank–van der Merwe misfit theory [S8]):

$$
E _ {\text {total}} = \langle V (\mathbf {r} + \mathbf {u} (\mathbf {r})) \rangle_ {\mathrm{AM}} + (1) / (2) \langle C _ {i j k l} \varepsilon_ {i j} (\mathbf {r}) \varepsilon_ {k l} (\mathbf {r}) \rangle_ {\mathrm{AM}}\tag{S1}
$$

![](images/0a74759ae39bb8eb561ee8ff5d39f6f3a4a59fb3a5d2baec336b91a7d6652d48.jpg)

![](images/2e4f9e16f59bc10dd6a25611dfe3d213b6ea7821d8b4976c3bb5bad5b1a2d77a.jpg)

![](images/ac6f592ef64c34ba1b4aca3e337f8b99e88b78e7214daca10cc52209943a30eb.jpg)  
Figure S3. Additional h-CuI/BLG(ann.) crystal with reversed epitaxial alignment (Sample 5). (a) ${ \sf C } _ { \sf c } / { \sf C } _ { \sf s }$ -corrected 80 kV HRTEM image of an h-CuI crystal within bilayer graphene after annealing; inset: FFT of the substrate region confirming bilayer nature (G, G′). (b) FFT of the heterostructure region showing that h-CuI (red dashed hexagon) aligns with G at a 30° rotation $( \Theta \approx 0 ^ { \circ } )$ , while $\boldsymbol { \mathsf { G } ^ { \prime } }$ appears as a separate hexagonal pattern. (c) Structure model of h-CuI encapsulated within bilayer graphene, shown in top and side view.

where $\langle . . . \rangle _ { \mathsf { A M } }$ is the moiré-cell average, V the registry potential, u(r) the in-plane relaxation field, and $\mathsf { C } _ { \mathrm { i j k l } }$ the 2D-elastic tensor. Assuming a rigid layer (uniform strain $\varepsilon _ { \mathrm { i j } } ,$ no in-cell relaxation $\mathsf { u } ( \mathsf { r } ) = \mathsf { u } _ { 0 } )$ , the registry average reduces to a discrete lock-in approximation:

$$
\langle V (\mathbf {r} + \mathbf {u} _ {0}) \rangle \approx - E _ {v d W} - \Delta U _ {P} f _ {l o c k}\tag{S2}
$$

with $\mathsf { f } _ { \mathsf { l o c k } } \in [ 0 , 1 / 3 ]$ for incommensurate registry, [1/3, 1/2] for uniaxial commensurate, and 1 for biaxial commensurate (the bounds reflect the Pokrovsky–Talapov continuum result). With the 2D elastic strain energy $\mathsf { F } _ { \mathsf { s t r a i n } }$ (Section S4b), we obtain:

$$
E _ {t o t a l} = - E _ {v d W} - \Delta U _ {P} \cdot f _ {l o c k} + F _ {s t r a i n}\tag{S3}
$$

where $\mathsf { E } _ { \mathsf { v d W } }$ is the registry-independent van der Waals adhesion (positive, stabilizing), $\Delta \cup _ { \mathsf { P } }$ $\mathsf { f } _ { \mathsf { l o c k } }$ is the corrugation gain from commensurate lock-in $( \mathsf { f } _ { \mathsf { l o c k } }$ as defined above), and $\mathsf { F } _ { \mathsf { s t r a i n } }$ is the elastic strain energy (positive, destabilizing).

## S4b. Strain Energy Formulas

For the general 2D strain (experimental data with full tensor) [S9]:

$$
F = (E _ {2 D}) / (2 (1 - v ^ {2})) [ \varepsilon_ {x x} ^ {2} + \varepsilon_ {y y} ^ {2} + 2 v \varepsilon_ {x x} \varepsilon_ {y y} + 2 (1 - v) \varepsilon_ {x y} ^ {2} ]\tag{S4}
$$

For biaxial strain $( \mathfrak { E } _ { \mathrm { x x } } = \mathfrak { E } _ { \mathrm { y y } } = \mathfrak { E } , \mathfrak { E } _ { \mathrm { x y } } = 0 )$

$$
F _ {b i} = (E _ {2 D}) / (1 - v) \varepsilon^ {2}\tag{S5}
$$

For uniaxial strain along one lattice direction $( \mathfrak { E } _ { \times \times } = \mathfrak { E } , \mathfrak { E } _ { \vee \vee } = 0 , \mathfrak { E } _ { \times \vee } = 0 )$ , the laterally constrained upper estimate:

$$
F _ {\mathrm{uni}} ^ {\varepsilon} = (E _ {2 D}) / (2 (1 - v ^ {2})) \varepsilon^ {2}\tag{S6}
$$

This laterally constrained form $( \varepsilon _ { \mathrm { y y } } \approx 0 )$ is the upper estimate of the uniaxial strain cost, applicable when the stiffer graphene substrate $( \mathsf { E } _ { 2 \mathsf { D } } \mathsf { ^ { G r } }$ ≈ 340 N/m) suppresses lateral relaxation of the soft $h – C u l \ ( E _ { 2 \mathsf { D } } \approx 3 5 \ \mathsf { N } / \mathsf { m } _ { \mathsf { \Omega } }$ Table S3). In Eqs. (S6) and (S7) the superscript names the transverse quantity that is held fixed: ε for zero transverse strain, where the substrate constrains the layer laterally, and σ for zero transverse stress, where the layer is free to contract laterally by the Poisson amount.

For the laterally free case with full Poisson relaxation (uniaxial-stress limit, $\varepsilon _ { \times \times } = \varepsilon , \varepsilon _ { \vee } = - \vee \varepsilon$ 9 $\varepsilon _ { x y } = 0 )$ , consistent with the experimentally observed in-plane contraction $( \mathsf { b } _ { 1 } < \mathsf { a } _ { \mathsf { c u l } } = 4 . 1 9 \AA \AA$ for Samples 3 and 5, Table S1):

$$
F _ {\mathrm{uni}} ^ {\sigma} = (1) / (2) E _ {2 D} \varepsilon^ {2}\tag{S7}
$$

The strain anisotropy ratio is:

$$
(F _ {\mathrm{bi}}) / (F _ {\mathrm{uni}} ^ {\sigma}) = (2) / (1 - \mathrm{v}) = 3. 4 5\tag{S8}
$$

This anisotropy factor [Eq. (S8)] helps explain the preference for uniaxial adaptation observed experimentally.

The experimental in-plane lattice mismatch is $\delta \approx 1 . 6 7 \% ( \mathsf { a } _ { \mathsf { c u l } } = 4 . 1 9 \mathsf { A } , \sqrt { 3 } { \cdot } \mathsf { a } _ { \mathsf { G } } = 4 . 2 6 \mathsf { A } ,$ see Table S3), and the layer must take it up as a strain $\varepsilon = \delta$ . For this mismatch the three strain configurations above predict the following h-CuI lattice-vector lengths $( \mathsf { b } _ { 1 } , \mathsf { b } _ { 2 } ,$ , b<sub>3</sub> labeled in ascending order of length as in Table S1, with the strain axis along the largest vector; the two shorter vectors are at $60 ^ { \circ }$ to that axis and therefore lengthen by about a quarter of the applied strain even when the transverse strain vanishes) and anisotropy $\mathsf { A } _ { \mathrm { b } } = \mathsf { m a x } ( \mathsf { b } ) / \mathsf { m i n } ( \mathsf { b } )$

• Uniaxial, laterally constrained (no Poisson relaxation, $\mathsf { E q . } ( \mathsf { S 6 } ) ) \colon \mathsf { b } _ { 1 } = 4 . 2 0 8 \ \mathring { \mathsf { A } } , \mathsf { b } _ { 2 } = 4 . 2 0 8 \ \mathring { \mathsf { A } } .$ $\mathsf { b } _ { 3 } = 4 . 2 6 0 \mathring { \mathsf { A } } , \mathsf { A } _ { \mathsf { b } } = 1 . 0 1 2$

• Uniaxial, laterally free (full Poisson relaxation, Eq $. ( 5 7 ) : = 4 . 1 8 6 \mathring { \mathsf { A } } , \mathsf { b } _ { 2 } = 4 . 1 8 6 \mathring { \mathsf { A } } , \mathsf { b } _ { 3 } = 4 . 2 6 0$ Å, $\mathsf { A } _ { \mathsf { b } } = 1 . 0 1 8$

• Biaxial commensurate (stretched): $\flat _ { 1 } = \flat _ { 2 } = \flat _ { 3 } = 4 . 2 6 0 \mathring { \mathsf { A } } , \mathsf { A } _ { \mathsf { b } } = 1 . 0 0 0$

The uniaxial cost depends on how freely the monolayer contracts perpendicular to the relaxation direction and lies between the Poisson-relaxed value, $\mathsf { F } _ { \mathsf { u n i } } { } ^ { \sigma } \approx 0 . 3 0 \mathsf { m e V } / \mathring { \mathsf { A } } ^ { 2 } \ ( \mathsf { E q }$ (S7)), and the laterally constrained value, 0.37 $\mathsf { m e V } / \mathring { \mathsf { A } } ^ { 2 }$ (Eq. (S6)). The ratio of the two costs is $\mathsf { F } _ { \mathrm { b i } } / \mathsf { F } _ { \mathrm { u n i } } \mathrm { \mathrm { ^ { o } } } = 2 / ( 1 \mathrm { - v } ) = 3 . 4 5$ . The main text (Growth mechanism and phase selection) estimates limits for the effective corrugation between the lower uniaxial limit and the biaxial upper limit, $0 . 3 0 < \Delta \mathsf { U } _ { \mathsf { P , e f f } } < 1 . 0 5 \mathsf { m e V / \AA ^ { 2 } } ;$ this lies above the rigid-sliding upper bound of Table S3. The measured lattice anisotropy of the two annealed, graphene-aligned crystallites, $1 . 0 1 7 \pm$ 0.004 (Sample 4) and $1 . 0 1 9 \ : \pm \ : 0 . 0 0 4$ (Sample 5, Table S1), matches the laterally free prediction of 1.018 rather than the laterally constrained value of 1.012, so the uniaxial cost is quoted at the lower limit. The contraction seen in Sample $5 \left( \mathsf { b } \approx 4 . 1 8 \mathsf { \AA } < \mathsf { a } _ { \mathsf { C u l } } = 4 . 1 9 \mathsf { \AA } \right)$ , Table S1) confirms the perpendicular Poisson contraction.

## S4c. Van der Waals Adhesion: Direct DFT and Literature Cross-Check

The primary adhesion values used in the main text were obtained by direct DFT in the untwisted 3 × 3 h-CuI on $5 \times 5$ graphene supercell, see the Methods section of the main text (VASP, PBE+D3 with Becke–Johnson damping; 18 Cu, 18 I and 50 C atoms; rhombic cell, $\mathsf { A } =$ 131.4 $\mathring { \mathsf { A } } ^ { 2 } )$ . The adhesion was evaluated as $\mathsf { E } _ { \mathrm { v d W } } = [ \mathsf { E } ( \mathsf { G r } ) + \mathsf { E } ( h \mathrm { - C u l } ) - \mathsf { E } ( \mathsf { h e t e r o } ) ] / \mathsf { A }$ . The calculated values are 13.58 meV/Å<sup>2</sup> $( 0 . 2 1 8 \mathsf { J } / \mathsf { m } ^ { 2 } )$ for pristine graphene and 13.65 $\mathsf { m e V } / \mathring { \mathsf { A } } ^ { 2 }$ for defective graphene.

Note on the $\Delta \cup _ { \mathsf { P } }$ uncertainty in Table S3. The Gr–CuI corrugation potential $\Delta \cup _ { \mathsf { P } }$ is reported as 0.01–0.14 $\mathsf { m e V } / \mathring { \mathsf { A } } ^ { 2 }$ (central value 0.07). The upper bound of this range is derived from Ullah et al. [S11], who computed the registry-dependent stacking energy of CuI encapsulated by graphene by sliding and rotating the layers across five distinct configurations and found the total energy variation to be $\rangle < 0 . 3$ meV/atom (DFT, vdW-DF1/optPBE-vdW). Their supercell contains 14 atoms (12 graphene $\hphantom { - } \mathsf { C } + \mathsf { 2 }$ CuI atoms) over an area $\mathsf { A } = ( \sqrt { 3 / 2 } ) { \cdot } \mathsf { a } _ { \mathrm { C u l } } { } ^ { 2 } \approx 1 5 { \cdot } 2 0 \AA ^ { 8 / 2 }$ with two equivalent CuI/graphene interfaces, yielding a total per-area span $\leq 0 . 3 \times 1 4 / 1 5 . 2 0 \approx$ 0.276 $\mathsf { m e V } / \mathring { \mathsf { A } } ^ { 2 }$ for the encapsulated cell, $\mathsf { o r } \le 0 . 1 4 \mathsf { m e V } / \mathring { \mathsf { A } } ^ { 2 }$ per single CuI/graphene interface as relevant for the one-sided geometry studied here. This per-interface DFT span sets the upper end of the quoted range $( 0 . 1 4 \mathrm { { m e V } } / \mathring { \mathsf { A } } ^ { 2 } )$ ; the lower end of the range (0.01 meV/Å<sup>2</sup>) is not obtained by subtraction but represents the physical floor of the vanishing-corrugation regime consistent with the experimentally observed soft twist-angle degree of freedom. The same uncertainty range propagates to all derived quantities involving $\Delta \cup _ { \mathsf { P } }$

A sensitivity analysis of the $\gamma  \beta$ phase penalty covering the literature-bulk range and a conservative 2×-bulk upper bound is included in Table S4. The freestanding open monolayer lies about 20.5 meV/Å<sup>2</sup> above bulk $\gamma { - } \mathsf { C u l }$ , 17.4 meV/Å<sup>2</sup> for the CuI–CuI interlayer bond. One graphene interface (13.58 meV/Å<sup>2</sup>) reduces the energy difference of h-CuI and bulk $\gamma { \mathrm { - C u l } }$ however leaving the h-CuI/SLG heterostructure still about $+ 7 . 0 \mathrm { \ m e V } / \mathring { \mathsf { A } } ^ { 2 }$ above γ (metastable, kinetically trapped); a second interface further reduces the energy difference to −6.6 meV/Å<sup>2</sup> (thermodynamically favored).

## S4d. Adhesion in the Presence of an Interfacial Gap

To evaluate the effect of interfacial adlayers, the sheet–sheet interaction is modeled with the planar potential [S14], $\mathsf { E } _ { \mathrm { v d W } } ( z ) = \mathsf { E } _ { 0 } [ ( 5 / 3 ) ( z _ { 0 } / z ) ^ { 4 } - ( 2 / 3 ) ( z _ { 0 } / z ) ^ { 1 0 } ]$ . This form is calibrated to the direct-DFT depth $\mathsf { E } _ { 0 } = 1 3 . 5 8 \mathsf { m e V } / \mathring { \mathsf { A } } ^ { 2 }$ at the equilibrium gap $Z _ { 0 } = 3 . 6 8 \mathring { \mathsf { A } }$ . Its curvature at ${ \cal Z } _ { 0 }$ gives the interfacial van der Waals spring constant, $\mathsf { k } = 4 0 ~ \mathsf { E } _ { 0 } / \mathsf { z } _ { 0 } { } ^ { 2 } \approx 4 0 ~ \mathsf { m e V } / \mathsf { \AA } ^ { 4 } = 6 . 4 \times 1 0 ^ { 1 9 } ~ \mathsf { N } / \mathsf { m } ^ { 3 }$ With the areal mass of the h-CuI sheet, 25.9 amu/Å<sup>2</sup>, and that of one graphene layer, 4.6 amu/Å<sup>2</sup>, the reduced areal mass is 3.9 amu/Å<sup>2</sup>, and the interfacial breathing mode follows as $\mathsf { f } = ( 1 / 2 \pi ) \sqrt { ( \mathsf { k } / \mu ) } = 1 . 5 9 \mathsf { T H z }$ . The adhesion decays steeply due to the $Z ^ { - 4 }$ tail. An interfacial layer, such as the adsorbed water layer, $3 . 7 \pm 0 . 2 \mathring { \mathsf { A } }$ thick [S15], that is ubiquitous on graphitic surfaces under ambient conditions [S16], is comparable to ${ \cal Z } _ { 0 }$ itself. Evaluating $\mathsf { E } _ { \mathsf { v d w } } ( \mathsf { Z } _ { 0 } + \Delta \mathsf { z } )$ for an additional gap $\Delta z = 2 . 8 \ – 3 . 7 \mathring { \mathsf { A } }$ gives $2 . 3 \ : \mathrm { m e V } / \mathring { \mathsf { A } } ^ { 2 }$ at $\Delta z = 2 . 8 \AA$ and $1 . 4 \ : \mathrm { m e V } / \mathring { \mathsf { A } } ^ { 2 }$ at $\Delta z = 3 . 7$ $\mathring { \mathsf { A } } ,$ that is 17% and 10% of $\mathsf { E } _ { 0 } .$ . Such an interfacial layer therefore strongly reduces the van der Waals stabilization required for growth of supported h-CuI.

Table S3. Lattice and DFT-input parameters used in the energy balance calculation.

<table><tr><td>Parameter</td><td>Symbol</td><td>Value</td><td>Unit</td><td>Source</td></tr><tr><td>In-plane stiffness</td><td> $E_{2D}$ </td><td>35</td><td>N/m</td><td>[S13] (DFT)</td></tr><tr><td>Poisson ratio</td><td>v</td><td>0.42</td><td>—</td><td>[S13] (DFT); directional range 0.40–0.44</td></tr><tr><td>h-Cul lattice constant</td><td> $a_{Cul}$ </td><td>4.19</td><td>Å</td><td>[S10] (DFT)</td></tr><tr><td>Graphene superlattice</td><td> $\sqrt{3} \cdot a_G$ </td><td>4.26</td><td>Å</td><td> $a_G = 2.460$  Å</td></tr><tr><td>Lattice mismatch</td><td>δ</td><td>1.67</td><td>%</td><td> $(\sqrt{3} \cdot a_G - a_{Cul})/a_{Cul}$ </td></tr><tr><td>Unit cell area</td><td> $A_{uc}$ </td><td>15.2</td><td>Å2</td><td> $\sqrt{3}/2 \cdot a_{Cul}^2$  (freestanding lattice; the cell contains two Cu and two I atoms)</td></tr><tr><td>Gr-Cul binding (direct DFT)</td><td> $E_{vdW}$ </td><td>13.58 (pristine) / 13.65 (defective)</td><td>meV/Å2</td><td>our DFT (Methods); net cross-check: 14.1 [S10]</td></tr><tr><td>Gr-Cul corrugation</td><td> $\Delta U_P$ </td><td>0.01–0.14 (central 0.07)</td><td>meV/Å2</td><td>DFT upper bound, Ullah et al. [S11]</td></tr></table>

Table S4. Thermodynamic parameters used in the main-text energy balance.

<table><tr><td>Parameter</td><td>Value</td><td>Source / method</td></tr><tr><td> $\gamma \rightarrow \beta$  phase penalty (bulk)  $\Delta E$ </td><td>3.0–3.4 (2×-bulk upper bound 6.6)</td><td>Yang et al. [S12] (bulk reference); conservative 2×-bulk upper bound for 2D correction</td></tr><tr><td>Cul/Gr corrugation  $\Delta U_P$ </td><td>0.01–0.14 (central 0.07) meV/ $\AA^2$ </td><td>DFT upper bound, Ullah et al. [S11]</td></tr><tr><td>Poisson ratio (h-Cul) v</td><td>0.42 ± 0.02</td><td>Demirok et al. [S13]</td></tr></table>

## S5. Analysis of the AIMD Trajectories

The AIMD trajectories analyzed here were produced with CP2K as described in the Methods section of the main paper, see Fig. S4. Each system was run as at least six restart segments of about 1.5 ps, at 300 and 600 K (Section S5b). Positions were cached every 5 fs, and the nuclear propagation time step was 0.5 fs. Velocities were obtained from the cached positions by central finite difference.

![](images/0c0c014f2d8dfb7cedff48df72837bcef45c0a6072a5ef447d8011cb200dd095.jpg)

![](images/40fcf2402f8a5e5e0a10aa28d4d1a09a1f7cf66a3f46d92e6c7082e685fb311e.jpg)

![](images/6f6977dd6f94a66e1bf302fe5e5cfd60390d082472f900374c79796c3838d4e4.jpg)

![](images/ff9caed241b7fd607dc1a83e1ee6681d6c7a03a6ce232e729f173f9298c8f921.jpg)

![](images/684f11f7b9cda851c90595096c9e4dcdb7540d0295c00f7663636bfcd21b2bfd.jpg)

![](images/b92484d60b66a51662410507d7d34180973a4d9f9d9356a20441a619dfbce067.jpg)

![](images/935fdb7ef06aa551218febf7ada35bd1468822bce1251964942f43f9e2bb8c85.jpg)

![](images/9bc700f1d14f6a156d4c63b59ca41f8b5298af65ba32fac0f0a450bef02c5d77.jpg)  
Figure S4. AIMD supercell geometry. Left column, top views; right column, side views. (a, b) h-CuI on single-layer graphene (SLG) at 300 K: the graphene lattice (gray) with overlaid h-CuI (Cu orange, I purple); the moiré stripe pattern is visible in the top view, and the side view shows one graphene layer on one side and vacuum on the other. (c, d) h-CuI within bilayer graphene (BLG) at 300 K: the mirrorsymmetric I–Cu–Cu–I sandwich (bilayer thickness 3.93 Å) between two graphene layers. (e, f) SLG at 600 K and (g, h) BLG at 600 K, in the same views. Supercell vectors $| \mathsf { R } _ { 1 } | = 2 4 . 9 9 \mathring { \mathsf { A } }$ $| \mathsf { R } _ { 2 } | = 2 9 . 0 4 \mathrm { \AA }$ , the angle between them $\mathsf { V } ^ { = 3 7 . 5 ^ { \circ } }$ , and the area $\mathsf { A } _ { \mathsf { c e l l } } = 4 4 1 . 7 \mathring { \mathsf { A } } ^ { 2 }$ are identical in all panels, as is the epitaxial twist angle $\theta = | 3 0 ^ { \circ } - \Delta | \approx 2 0 . 6 ^ { \circ }$ between the h-CuI and the graphene lattice, with $\Delta \approx 9 . 4 ^ { \circ }$ the angular difference between the nearest lattice vectors (Section S2c); only the number of graphene layers and the temperature differ. (Supercell geometry at $\mathrm { t } = 0 . 1 2 5$ ps (CP2K, PBE/GPW, nuclear propagation time step 0.5 fs).)

The cell holds six sublayers: the graphene layers $\mathsf { C } _ { \mathsf { b o t } }$ and $\mathsf { C } _ { \mathsf { t o p } }$ , the copper sublayers $\mathsf { C u } _ { \mathsf { b o t } }$ and $\mathsf { C u } _ { \mathsf { t o p } } .$ , and the iodine sublayers I<sub>bot</sub> and $\mathsf { I } _ { \mathsf { t o p } }$ of the I–Cu–Cu–I sandwich. The supported cell has no $\mathsf { C } _ { \mathsf { t o p } }$ . The collective coordinates read in Fig. 6 of the main paper are defined as follows.

$Z _ { \mathrm { a n t i } } ~ = ~ \sqrt [ 1 ] { _ { 2 } ( \bar { Z } _ { \mathrm { t o p } } ~ - ~ \bar { Z } _ { \mathrm { b o t } } ) }$ , the antisymmetric out-of-plane coordinate of the two CuI sublayers, formed from their center-of-mass heights.

${ \sf T O } = \bar { \sf V } _ { \sf y } ( { \sf C u } ) - \bar { \sf V } _ { \sf y } ( { \sf I } )$ , the in-plane transverse optical coordinate, formed from the centerof-mass velocities of the copper and of the iodine sublattice as a whole.

• The coherence of Fig. 6(c) combines the center-of-mass height of a graphene layer with that of the adjacent CuI sublayer.

Power spectra were formed per restart segment. The coordinate was multiplied by a Hann window, zero-padded to 8192 samples and Fourier-transformed. The segment spectra were averaged with weights equal to their post-equilibration length, at least 200 frames each. The mean was then scaled to its own maximum, taken over 0–5.6 THz in Fig. 6(a) and over 1.5– 6.5 THz in Fig. 6(b). Both spectra are plotted unsmoothed.

For the coherence the auto- and cross-spectra were accumulated with the same weights. The squared coherence $\mathsf { Y } ^ { 2 } = \vert \mathsf { S } _ { \mathsf { A B } } \vert ^ { 2 } / ( \mathsf { S } _ { \mathsf { A A } } \mathsf { S } _ { \mathsf { B B } } )$ was formed after the average and smoothed with a 0.10 THz Gaussian. The band positions, spectral weights and coherences read from Fig. 6(a)–(c) are collected in Table S5.

In Fig. 6 of the main paper, a frequency is resolved in a segment-averaged spectrum only if every contributing segment holds at least one full period of it. As the individual segments give 1/T between 0.39 and 0.85 THz, the resolution limit of a run is set by the largest of these, 0.85 THz.

Mean-square displacements were averaged over time origins within each segment and then over segments. The plateau values of Fig. 6(i) are averages over lag times $\tau = 0 . 3 \mathrm { - } 1 . 0 \ p s$ . The in-plane plateau values are collected in Table S6, and the top-over-bottom sublayer ratios for both species and both directions in Table S7. The out-of-plane displacements of Fig. 6(g) and 6(h) are resolved by sublayer after removing the center-of-mass motion of that sublayer, so they measure internal roughness. For a bound atom the plateau equals $2 \sigma _ { z } ^ { 2 }$ , so the amplitude follows as $\sigma _ { z } = \sqrt { ( \mathsf { M S D } / 2 ) }$

Fig. S5 shows the full frequency range, including the region below 0.9 THz, which carries less statistical weight. The supported h-CuI sheet follows the out-of-plane motion of its graphene layer more closely than either pair of the encapsulated cell.

![](images/1af550efcc56ec0951946bfa0cff7cf37b381a7e68f5102817723b6a2b1151e1.jpg)

![](images/4ead5bf54ec2779aa723c34a2fe6b531d303448000a09c5a1cbf180506fe7eec.jpg)

![](images/737a4541f305f6e0579207d26423e4f2a01d3f0f22d7fbed96b15e9c3373f6ff.jpg)

![](images/fde135cbbf8db0a36b9a63c9d75f7af94e76efdc73ef9fe45755c0a81ea88e32.jpg)  
Figure S5. Squared spectral coherence between the out-of-plane center-of-mass coordinate of a graphene layer and that of the adjacent CuI sublayer, for h-CuI on single-layer graphene and within bilayer graphene, with the bottom and the top pair shown separately. Spectra are segment-averaged as described in Section S5a and smoothed with a 0.10 THz Gaussian; the region below 0.9 THz lies at or below the resolution limit of the individual restart segments and is shown for completeness only. (a) Bottom pair, bottom graphene against the bottom CuI sublayer, for all four systems. (b) Top pair, top graphene against the top CuI sublayer, encapsulated cell at both temperatures. Solid lines are 300 K and dashed lines 600 K. The shaded interval marks 1.0–1.7 THz, where the curvature of the adhesion potential of Eq. (2) of the main text places the interfacial breathing mode at 1.59 THz.

Table S5. Spectral quantities read from Fig. 6(a)–(c), with uncertainties over the restart segments. SLG is the supported cell and BLG the encapsulated cell. Spectral weight is the mean of the normalized power spectrum over the interval given. Band positions are maxima of the segmentaveraged spectra, and the two positions of the internal Cu–I band agree within their uncertainties.

<table><tr><td>Quantity</td><td>SLG</td><td>BLG</td></tr><tr><td> $Z_{anti}$  main band (internal Cu–I), 300 K [THz]</td><td>3.93 ± 0.22</td><td>4.20 ± 0.08</td></tr><tr><td>In-plane band TO, maximum, 300 K [THz]</td><td>1.93 ± 0.21</td><td>2.76 ± 0.05</td></tr><tr><td>In-plane band TO, maximum, 600 K [THz]</td><td>1.86 ± 1.06</td><td>2.66 ± 1.23</td></tr><tr><td> $\gamma^{2}$ , 0.9–3.0 THz, 300 K</td><td>0.525 ± 0.050</td><td>0.083 ± 0.134 (bottom pair), 0.206 ± 0.176 (top pair)</td></tr><tr><td> $\gamma^{2}$ , 1.0–1.7 THz, 300 K</td><td>0.656 ± 0.067</td><td>0.101 ± 0.317 (bottom pair), 0.070 ± 0.091 (top pair)</td></tr></table>

Table S6. In-plane mean-square displacement of copper and of iodine, averaged over lag times τ = 0.3–1.0 ps and over the restart segments (Fig. 6(f)). SLG is the supported cell and BLG the encapsulated cell.

<table><tr><td>Species</td><td>SLG 300 K</td><td>SLG 600 K</td><td>BLG 300 K</td><td>BLG 600 K</td></tr><tr><td> $Cu\ MSD_{xy}$ [Å2]</td><td>0.193</td><td>0.655</td><td>0.207</td><td>0.582</td></tr><tr><td> $I\ MSD_{xy}$ [Å2]</td><td>0.085</td><td>0.220</td><td>0.093</td><td>0.169</td></tr></table>

Table S7. Sublayer ratios of the mean-square displacement, top sublayer over bottom sublayer, for both species and both directions. SLG is the supported cell and BLG the encapsulated cell. Each ratio is formed within one run. In the supported cell the bottom sublayer is in contact with graphene and the top faces vacuum. In the encapsulated cell both are in contact, so its columns are the control.

<table><tr><td>Quantity</td><td>SLG 300 K</td><td>SLG 600 K</td><td>BLG 300 K</td><td>BLG 600 K</td></tr><tr><td>I, out of plane</td><td>1.218 ± 0.048</td><td>1.301 ± 0.029</td><td>1.036 ± 0.030</td><td>0.952 ± 0.059</td></tr><tr><td>I, in plane</td><td>0.951 ± 0.063</td><td>0.934 ± 0.031</td><td>0.998 ± 0.046</td><td>0.978 ± 0.020</td></tr><tr><td>Cu, out of plane</td><td>0.903 ± 0.028</td><td>0.967 ± 0.050</td><td>1.046 ± 0.047</td><td>0.971 ± 0.070</td></tr><tr><td>Cu, in plane</td><td>1.170 ± 0.120</td><td>0.991 ± 0.036</td><td>0.955 ± 0.108</td><td>1.226 ± 0.188</td></tr><tr><td>I  $MSD_z$ , bottom / top [Å2]</td><td>0.055 / 0.067</td><td>0.126 / 0.164</td><td>0.056 / 0.058</td><td>0.133 / 0.126</td></tr><tr><td>Cu  $MSD_z$ , bottom / top [Å2]</td><td>0.081 / 0.073</td><td>0.248 / 0.240</td><td>0.076 / 0.079</td><td>0.242 / 0.235</td></tr></table>

The trajectories cover 300 and 600 K in one commensurate supercell, on restart segments of about 1.5 ps. Within these segments the iodine displacement reaches a plateau in both directions, while the copper in-plane displacement continues to rise. Amplitude comparisons between two separate runs carry the full segment scatter, and the copper inplane difference between the supported and the encapsulated cell at 600 K stays within it. The quantities compared between the two cells in the main text are band positions, bandaveraged spectral weights and window-averaged coherences, which are stable over the segments (Section S5b). Time scales beyond the restart segments are outside the reach of these trajectories.

## Supporting References

[S1] Eigler, S.; Enzelberger-Heim, M.; Grimm, S.; Hofmann, P.; Kroener, W.; Geworski, A.; Dotzer, C.; Röckert, M.; Xiao, J.; Papp, C.; Lytken, O.; Steinrück, H.-P.; Müller, P.; Hirsch, A. Wet Chemical Synthesis of Graphene. Adv. Mater. 2013, 25, 3583–3587.

[S2] Eigler, S.; Hirsch, A. Chemistry with Graphene and Graphene Oxide—Challenges for Synthetic Chemists. Angew. Chem. Int. Ed. 2014, 53, 7720–7738.

[S3] Jia, G.; Plentz, J.; Presselt, M.; Dellith, J.; Dellith, A.; Patze, S.; Tölle, F. J.; Mülhaupt, R.; Andrä, G.; Falk, F.; Dietzek, B. A Double Self-Assembly Process for Versatile Reduced-Graphene-Oxide Layer Deposition and Conformal Coating on 3D Structures. Adv. Mater. Interfaces 2017, 4, 1700758.

[S4] Linck, M.; Hartel, P.; Uhlemann, S.; Kahl, F.; Müller, H.; Zach, J.; Haider, M.; Niestadt, M.; Bischoff, M.; Biskupek, J.; Lee, Z.; Lehnert, T.; Börrnert, F.; Rose, H.; Kaiser, U. Chromatic A<sub>b</sub>erration Correction for Atomic Resolution TEM Imaging from 20 to 80 kV. Phys. Rev. Lett. 2016, 117, 076101.

[S5] Nord, M.; Vullum, P. E.; MacLaren, I.; Tybell, T.; Holmestad, R. Atomap: a new software tool for the automated analysis of atomic resolution images using two-dimensional Gaussian fitting. Adv. Struct. Chem. Imaging 2017, 3, 9.

[S6] Ma, T. TemCompanion: An open-source multi-platform GUI program for TEM image processing and analysis. SoftwareX 2025, 31, 102212.

[S7] Woods, C. R.; Britnell, L.; Eckmann, A.; Ma, R. S.; Lu, J. C.; Guo, H. M.; Lin, X.; Yu, G. L.; Cao, Y.; Gorbachev, R. V.; Kretinin, A. V.; Park, J.; Ponomarenko, L. A.; Katsnelson, M. I.; Gornostyrev, Yu. N.; Watanabe, K.; Taniguchi, T.; Casiraghi, C.; Geim, A. K.; Novoselov, K. S. Commensurate–incommensurate transition in graphene on hexagonal boron nitride. Nat. Phys. 2014, 10, 451–456.

[S8] Frank, F. C.; van der Merwe, J. H. One-dimensional dislocations. I. Static theory. Proc. R. Soc. Lond. A 1949, 198, 205–216.

[S9] Peng, Z.; Chen, X.; Fan, Y.; Srolovitz, D. J.; Lei, D. Strain engineering of 2D semiconductors and graphene: from strain fields to band-structure tuning and photonic applications. Light Sci. Appl. 2020, 9, 190.

[S10] Mustonen, K.; Hofer, C.; Kotrusz, P.; et al. Toward Exotic Layered Materials: 2D Cuprous Iodide. Adv. Mater. 2022, 34, 2106922.

[S11] Ullah, S.; Thonhauser, T.; Menezes, M. G. Optoelectronic Properties of Novel Layered Materials under Encapsulation: 2D Copper Iodide and Silver Iodide. Appl. Mater. Today 2024, 41, 102495.

[S13] Demirok, A. C.; Sahin, H.; Yagmurcukardes, M. Ultra-thin double-layered hexagonal CuI: strain tunable electronic properties and robust semiconductor behavior. J. Phys.: Condens. Matter 2024, 36, 215401.

[S12] Yang, W.; Wang, Y.; Yi, S.; Zhang, D.; Liu, J.; Li, C.; Wang, J.; Fan, Z. Structure of β-CuI: Stacking of 2D Bilayers. Chem. Mater. 2024, 36, 829–837.

[S14] Gould, T.; Gray, E.; Dobson, J. F. Van der Waals dispersion power laws for cleavage, exfoliation, and stretching in multiscale, layered systems. Phys. Rev. B 2009, 79, 113402.

[S15] Xu, K.; Cao, P.; Heath, J. R. Graphene Visualizes the First Water Adlayers on Mica at Ambient Conditions. Science 2010, 329, 1188–1191.

[S16] Garcia, R. Interfacial Liquid Water on Graphite, Graphene, and 2D Materials. ACS Nano 2023, 17, 51–69.