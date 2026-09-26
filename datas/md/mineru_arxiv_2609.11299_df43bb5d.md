# A Two-Mirror Faceted Projection System for EUV Lithography

Vasiliy A. Es’kin<sup>∗</sup>, Egor V. Ivanov, Olga V. Martynova Department of Radiophysics, University of Nizhny Novgorod 23 Gagarin Ave., Nizhny Novgorod 603022, Russia vasiliy.eskin@gmail.com, iev90078@gmail.com, ruvin@list.ru

![](images/f7673938014d5c318d46809c102b7f0105124ff40e3dde38e751834312f6b362.jpg)

Happiness for everybody, free, and no one will go away unsatisfied!

Arkady and Boris Strugatsky, Roadside Picnic

## Abstract

We propose an all-reflective two-mirror projection system for extreme ultraviolet (EUV) lithography operating at exposure wavelengths of 13.5 nm $\mathrm { ( M o / S i ) }$ and 11.2 nm $\mathrm { ( R i u / B e ) }$ delivering a fourfold (4×) demagnification of the periodic mask pattern at a numerical aperture approaching unity $\left( \mathrm { N A } _ { \mathrm { m a x } } \approx 0 . 9 9 3 \right)$ . In contrast to conventional EUV projection objectives that incorporate 6–10 aspheric mirrors with an overall optical throughput of less than 15%, the proposed design redirects each accepted discrete spatial difraction order scattered by the mask onto the wafer via a dedicated pair of planar mirror facets. The number of reflections is strictly fixed at two for all accepted orders, retaining 50–60% of the power leaving the mask in each accepted order. We derive a spatial geometry providing rigorous optical path length equalization across all difraction orders, thereby removing order-dependent propagation phase shifts. Individually optimized 30-bilayer Bragg multilayer coatings are designed for each facet using the transfer matrix method combined with global evolutionary optimization algorithms. The architecture is generalized to a three-dimensional vector formulation with a two-dimensionally periodic mask. Utilizing inverse lithography technology, Fourier parameterization, and a diferentiable electromagnetic modal waveguide solver, we solve the synthesis problem for binary absorber masks (La absorber on a Ru/Be/Sr multilayer mirror). We demonstrate simulated aerial images of sub-10-nm features on the wafer (isolated peaks with a full width at half maximum (FWHM) of approximately 5.4 nm and line pairs with a critical dimension of 6 nm) and find that the two peaks remain resolved for the tested wafer defocus values from 0 to 5 nm along the z-axis.

Keywords Extreme Ultraviolet Lithography · Two-mirror projection system · High numerical aperture Multilayer Bragg mirrors · Inverse Lithography Technology · Waveguide method · RCWA · Computational physics · Machine Learning

## 1 Introduction

The modern technological world critically depends on semiconductor microchips, which lie at the heart of smartphones and personal computers, control automobiles and industrial robotics, route global internet trafic, and serve as the physical foundation for the ongoing wave of artificial intelligence systems. Global demand for computation, telecommunications, and machine perception is expanding at an explosive pace, and microelectronics has met this challenge for over half a century by doubling the number of active components on a chip approximately every two years in accordance with Moore’s Law [1]. At the foundation of this exponential progress lies the continuous downscaling of physical device dimensions, directly tied to the miniaturization of the individual transistor: smaller transistors yield higher integration density, superior operational speed, and enhanced energy eficiency. Optical photolithography serves as the primary engine of this miniaturization. It transfers the topology of the integrated circuit layout from a photomask onto a silicon wafer, thereby dictating the minimum printable feature size. The critical role of this tool in the economics of semiconductor manufacturing is reflected in its capital cost: while a 193-nm immersion lithography scanner costs on the order of 50 million euros, a state-of-the-art EUV scanner exceeds 300 million euros [2].

The minimum feature size printable via photolithography is fundamentally constrained by physical laws and obeys Rayleigh’s resolution equation, $\mathrm { { \dot { C D } = k _ { 1 } \lambda / \bar { N A } } }$ , where CD is the critical dimension, $k _ { 1 }$ is a processdependent factor (with a theoretical physical limit of 0.25), λ is the exposure wavelength, and NA is the numerical aperture of the projection optics [1]. As is evident from this fundamental relationship, shrinking feature dimensions requires either reducing the exposure wavelength or increasing the numerical aperture. Over six decades, the exposure wavelength transitioned from 436 nm (mercury g-line) through 365, 248, and 193 nm down to 13.5 nm, while the numerical aperture in liquid immersion systems surpassed unity to reach 1.35 [1, 3]. Along this developmental trajectory, lithographers adopted advanced techniques, such as of-axis illumination (OAI) and multiple patterning. In 2018, EUV lithography became commercially viable for high-volume manufacturing following the introduction of reliable 13.5-nm plasma sources delivering output powers exceeding 125 W [1].

The operational wavelength of 13.5 nm was selected because periodic Mo/Si Bragg multilayer coatings composed of 40–50 bilayers exhibit record near-normal reflectivities of ∼ 70% per mirror surface [4], and commercial scanner sources now deliver powers exceeding 400 W [5]. Standard NXE scanners operating at $\mathrm { N A } = 0 . 3 3$ print a minimum half-pitch of 13 nm, serving as the core workhorses of high-volume semiconductor manufacturing. The subsequent generation of High-NA EXE:5000 systems, with $\mathrm { N A } = 0 . 5 5$ , pushes the resolution down to 8 nm. However, this is achieved via an anamorphic projection architecture $\bar { ( 4 \times \textmd { / 8 } \times ) }$ in which the depth of focus (DoF) is reduced by a factor of 2.94, the exposure field size is halved, and mirror angles of incidence are constrained by the narrow angular reflectance bandwidth of $\mathrm { M o } / \mathrm { S i }$ coatings (±11<sup>◦</sup>) [1, 6–8]. Further increasing the numerical aperture to $\mathrm { \bar { N } A } = 0 . 7 5$ and beyond, as required for printing critical dimensions below 6 nm, will necessitate an even greater number of mirrors within the all-reflective projection channel [7, 9].

Each reflection in the illumination and projection optics absorbs a substantial fraction of the incident EUV power [2]. This motivates alternative wavelengths, including 11.2 nm with Ru/Be coatings and Xe-discharge sources [2, 10], short-wavelength multilayers in the 9–12 nm band [4, 11, 12], and architectures with fewer reflections. Shintake [9] compares a conventional system with four illumination and six projection reflections with a proposed system having two illumination and two projection reflections. At an assumed reflectance of 0.65 per surface, the corresponding transmissions are $\dot { 0 } . 6 \dot { 5 } ^ { 1 0 } \approx 1 . 3 \%$ and $0 . 6 5 ^ { 4 } \approx 1 8 \%$ . The associated estimate of a reduction from 1 MW to approximately 80 kW concerns electricity used for EUV generation, not the total scanner consumption. A later four-mirror in-line design [13] uses repeated encounters with its physical mirrors, giving eight reflections for $\mathrm { N A } = 0 . 5$ and twelve for $\mathrm { N A } \dot { = } 0 . 7$ . Mirror count must therefore be distinguished from reflection count.

The design of the reflective optical systems described above relies, in most cases, on geometric ray-tracing methods, which represent crude approximations of electromagnetic wave propagation that neglect wave phenomena such as interference and difraction. Incorporating difractive elements directly into the projection optics has been explored previously. For instance, in a three-mirror all-reflective scheme operating at 13 nm, aspheric mirrors were replaced by reflection difraction gratings on spherical substrates [14], and later this line of research was extended using reflective Fresnel zone plates [15, 16]. However, in those systems the difractive structure merely reproduces the phase profile of an aspheric mirror, the total number of reflections within the channel is not reduced, and stringent monochromaticity requirements are imposed on the source. Separately, maskless EUV lithography concepts based on arrays of micro-electromechanical mirrors have been proposed as alternatives to physical masks [17], addressing mask cost, defect, and pellicle challenges, though requiring their own specialized projection architectures.

In this work, we develop an alternative concept that pushes the reduction of reflective surfaces to its logical limit. We propose a two-mirror all-reflective projection system in which each spatial difraction order scattered by the mask is redirected onto the wafer individually by a dedicated pair of planar mirror facets. The number of reflections per accepted channel between the mask and wafer is fixed at two, independent of the numerical aperture. Thus, values of $\mathrm { N A } \sim 1$ are fundamentally attainable alongside a fourfold (4×) demagnification of the mask pattern. We consider both two-dimensional and three-dimensional problem formulations. In the 3D case, the mask represents a two-dimensionally periodic structure (a square grating), and each propagating difraction order is mapped to its own corresponding facet pair across both mirrors. The analysis is performed in an approximation close to geometrical optics (GO), where propagating spatial difraction orders are described as collimated paraxial beams with uniform cross-sectional amplitude.

The paper is structured as follows. In Section 2, the electromagnetic difraction problem for an EUV mask is formulated and the basic relations governing the two-mirror projection system are derived. Section 3 presents the two-dimensional two-mirror projection system, including the iterative design of the mirror geometry, the optimization of individually tuned Bragg multilayer coatings for each facet, and the synthesis of binary absorber masks for a target aerial image using inverse lithography technology with Fourier-parameterized projection. Section 4 extends the formulation to three dimensions, generalizing the design to a two-dimensionally periodic mask with a square lattice and demonstrating 3D mask synthesis. Section 5 discusses the advantages and disadvantages of the proposed projection system. Finally, in Section 6 concluding remarks are given. Appendix A provides a rigorous analysis of the validity of the geometrical-optics beam approximation for centimeter-scale EUV beams.

## 2 Formulation of the Problem

We begin by examining the electromagnetic difraction problem for an EUV mask in a two-dimensional formulation, subsequently extending the analysis to the structural design of a projection system providing a 4× demagnification of the mask pattern onto the wafer.

The layered mask, consisting of J layers, occupies the domain $[ - D , 0 ]$ along the z-axis and $[ - L / 2 , L / 2 ]$ along the x-axis in a Cartesian coordinate system $( x , y , z )$ , as illustrated in Fig. 1, and is periodic along the x-direction with spatial period $L _ { x }$ . Each layer $j$ is homogeneous along the z-direction and has a complex permittivity $\varepsilon _ { j } = \varepsilon _ { j } ( x )$ ). Optical constants are obtained from tabulated reference data [18, 19]. Within the mask stack, one distinguishes patterned absorber (or phase-shifting) layers that define the composition of the scattered spectrum, and the underlying multilayer Bragg mirror substrate (see Fig. 2). Here, the multilayer substrate is assumed to consist of periodic three-component Ru/Be/Sr stacks [20] or two-component Ru/Be (or Mo/Si) bilayers [4, 11, 12].

The primary objective is to construct an all-reflective projection system that provides a 4× demagnification of the mask pattern when projected onto the wafer. Under 4× reduction, the spatial period on the wafer, $L _ { x } ^ { \mathrm { ( w ) } }$ , satisfies $L _ { x } ^ { \mathrm { ( w ) } } = L _ { x } / 4 ( \mathrm { i . e . , } L _ { x } = 4 L _ { x } ^ { \mathrm { ( w ) } } )$ , where both the wafer plane and the mask plane are assumed to be parallel to the $x O y$ plane. Pattern transfer from the mask to the wafer is mediated by the electromagnetic field scattered by the mask and focused onto the wafer.

Assuming the lateral mask dimension satisfies $L \gg L _ { x }$ , edge efects can be neglected, allowing the mask to be treated as an infinite periodic structure during the difraction analysis. A TE-polarized monochromatic plane wave with angular frequency ω is obliquely incident on the mask. In the geometrical-optics (GO) beam approximation, the field amplitude is uniform within the beam envelope and zero elsewhere. The incident electric field is given, with $\exp ( \mathrm { i } \omega t )$ time dependence dropped, by $\mathbf { E } ^ { ( i ) } = \mathbf { y } _ { 0 } E _ { 0 } \exp \left[ - \mathrm { i } ( \tilde { m } \kappa _ { x } x - k _ { z } ^ { ( i ) } z ) \right]$ where $E _ { 0 }$ is the electric field amplitude, $\tilde { m } \kappa _ { x }$ and $k _ { z } ^ { \left( i \right) }$ are the components of the wave vector $\mathbf { k } _ { 0 }$ in free space $( k _ { 0 } = \bigg \lceil \tilde { m } ^ { 2 } \kappa _ { x } ^ { 2 } + \Big ( k _ { z } ^ { ( i ) } \Big ) ^ { 2 } \bigg \rceil ^ { 1 / 2 } , \kappa _ { x } = 2 \pi / L _ { x } , k _ { 0 } = \omega / c$ , where c is the speed of light in free space), and superscript (i) denotes the incident wave. The resulting boundary-value difraction problem is solved using modal numerical methods [20–25]. The scattered electric field in the vicinity of the mask is expanded in a series:

$$
E _ {y} ^ {(r)} = \sum_ {m = - \infty} ^ {\infty} A _ {m} ^ {(r)} \exp (- \mathrm{i} \kappa_ {x} m x - \mathrm{i} k _ {z; m} z),\tag{1}
$$

where $A _ { m } ^ { ( r ) }$ is the complex amplitude of the m-th scattered spatial harmonic, and $k _ { z ; m } = \left( k _ { 0 } ^ { 2 } - \kappa _ { x } ^ { 2 } m ^ { 2 } \right) ^ { 1 / 2 }$ (choosing the branch Im $k _ { z ; m } \leq 0 )$ .

For the projection-system design, only propagating difraction orders (purely real $k _ { z ; m } )$ are relevant. Thus, the scattered field of interest outside the near-field region of the mask is:

$$
E _ {y} ^ {(r)} = \sum_ {m = - M} ^ {M} \tilde {A} _ {m} ^ {(r)} (x, z) \exp (- \mathrm{i} \kappa_ {x} m x - \mathrm{i} k _ {z; m} z),\tag{2}
$$

where $\tilde { A } _ { m } ^ { ( r ) } ( x , z ) = A _ { m } ^ { ( r ) }$ inside the spatial beam corresponding to order m (see Fig. 1), and $\tilde { A } _ { m } ^ { ( r ) } ( x , z ) = 0$ outside it. The maximum propagating order index is $\bar { M } = \lfloor k _ { 0 } \bar { / } \kappa _ { x } \rfloor$

To achieve a $4 \times$ demagnified aerial image on the wafer, the propagating field spectrum at the wafer boundary must take the form:

$$
E _ {y} ^ {\mathrm{(w)}} = \sum_ {n = - N} ^ {N} B _ {n} \exp \Bigl [ - \mathrm{i} \kappa_ {x} ^ {\mathrm{(w)}} n x - \mathrm{i} s _ {\mathrm{w}} k _ {z; n} ^ {\mathrm{(w)}} \zeta_ {\mathrm{w}} \Bigr ],\tag{3}
$$

where $\zeta _ { \mathrm { w } } = z - Z _ { \mathrm { w } }$ is measured from the wafer plane, $s _ { \mathrm { w } } = + 1$ in Examples 1, 3, and 4 and $s _ { \mathrm { w } } = - 1$ in Example 2, and $B _ { n }$ is the complex amplitude of the n-th harmonic at $\zeta _ { \mathrm { w } } = 0 , \kappa _ { x } ^ { \mathrm { ( w ) } } = 2 \pi / L _ { x } ^ { \mathrm { ( w ) } }$ , and $k _ { z ; n } ^ { \mathrm { ( w ) } } = \left\lceil k _ { 0 } ^ { 2 } - ( \kappa _ { x } ^ { \mathrm { ( w ) } } ) ^ { 2 } n ^ { 2 } \right\rceil ^ { 1 / 2 }$ . Under 4× reduction, the maximum propagating order transmitted to the wafer is $N = \left\lfloor M / 4 \right\rfloor$ (ideally $\mathbf { \bar { \mathit { M } } } = 4 N $ ; the diference arises from the cutof of orders $n > N$ as evanescent waves). Hence, the design task reduces to transforming the transverse spatial frequency of each m-th harmonic scattered by the mask into harmonic $n = - m$ on the wafer in the common Cartesian coordinate system:

$$
m \kappa_ {x} \longrightarrow - m \kappa_ {x} ^ {\mathrm{(w)}}.\tag{4}
$$

Because this spatial-frequency mapping is linear, it can be realized using a dual set of planar mirror facets. Specifically, the first mirror system redirects each m-th beam along a direction parallel to the $z \mathrm { - a x i s ~ } \left( \mathrm { F i g . ~ 3 } \right)$ whereupon the second mirror system redirects it toward the wafer at an angle corresponding to $k _ { x } = - m \kappa _ { x } ^ { \mathrm { ( w ) } }$ (Fig. 4). Figure 4 schematically illustrates the all-reflective system comprising two sets of planar mirror facets. The first set converts the divergent beams scattered by the mask into a parallel array of vertical beams. The second set redirects a subset of these parallel beams at the required convergence angles onto the wafer.

We note that because the illumination beam with spatial harmonic m˜ enters through an optical input aperture occupying the position corresponding to the −m˜ reflection order (back reflection), order $m = - \tilde { m }$ is omitted from the projected spectrum (Fig. 4). Thus, at the first reflection, the amplitude $\tilde { A } _ { - \tilde { m } } ^ { ( r ) } ( x , z )$ is multiplied by zero.

![](images/4f29448d0e53210711079bca13aebcba5b6acdcbc1aa91a1ce9a556021d20e53.jpg)  
Figure 1: Electromagnetic beam scattering by a lithographic mask (schematic in the geometrical-optics approximation).

(a)  
![](images/e3b63614e90692c20948a77751333fdba2e2bfbcd830a31bebad3fdf46e080fa.jpg)

(b)  
![](images/47bf24e13e6cbeda99f1a44562a56579603da7f2c77b8dbae5e3b3340a8c68cd.jpg)  
Figure 2: Geometry of the problem: (a) cross-section at $y = 0$ with mask spatial period $L _ { x } ,$ , (b) perspective view of the mask stack.

![](images/77b00be3e2a4df4b7f05e554a5fa1ccb28483d335bc6c0bbe423998da1206653.jpg)  
Figure 3: Reflection of the m-th difraction beam from a planar mirror facet into a direction antiparallel to the z-axis.

Referring to Fig. 3, the beam parameters and mirror facet orientation for vertical reflection satisfy:

$$
\begin{array}{l} \cos \alpha_ {m} = \frac {m \kappa_ {x}}{k _ {0}}, \\ a _ {m} = L \sin \alpha_ {m}, \\ \gamma_ {m} = \frac {\pi}{4} - \frac {\alpha_ {m}}{2}, \end{array}\tag{5}
$$

where $\alpha _ { m }$ is the angle of the m-th beam measured from the mask plane (horizontal), $a _ { m }$ is the beam cross-sectional width, and $\gamma _ { m }$ is the tilt angle of the facet $( \tau _ { m } = \gamma _ { m }$ in $\operatorname { F i g } . \ 3 )$ . Each m-th beam projects an illuminated footprint $L _ { m } ^ { \mathrm { ( w ) } }$ on the wafer plane given by:

$$
a _ {m} = L _ {m} ^ {\mathrm{(w)}} \sin \alpha_ {m} ^ {\mathrm{(w)}},\tag{6}
$$

where sin $\alpha _ { m } ^ { \mathrm { ( w ) } } = k _ { z ; m } ^ { \mathrm { ( w ) } } / k _ { 0 }$ and $\alpha _ { m } ^ { \mathrm { ( w ) } }$ is the grazing angle at the wafer plane. Consequently:

$$
L _ {m} ^ {\mathrm{(w)}} = L \frac {k _ {z ; m}}{k _ {z ; m} ^ {\mathrm{(w)}}} = L \left(\frac {1 - \left(\frac {m \kappa_ {x}}{k _ {0}}\right) ^ {2}}{1 - 1 6 \left(\frac {m \kappa_ {x}}{k _ {0}}\right) ^ {2}}\right) ^ {1 / 2}.\tag{7}
$$

![](images/9bfb6e6217e6633867d6e2ba17ceb43cc93fef06e63c5bdb0b91778751df3547.jpg)  
Figure 4: Schematic of the all-reflective two-mirror faceted projection architecture.

To prevent beam crosstalk, each facet of the first mirror must intercept only its assigned difraction order. This requires that adjacent beam envelopes do not overlap at the mirror plane. The intersection point of the boundaries of adjacent orders m and m + 1 is derived from their ray equations:

$$
z = \frac {k _ {z ; m}}{\kappa_ {x} m} \left(x - \frac {L}{2}\right),
$$

$$
z = \frac {k _ {z ; m + 1}}{\kappa_ {x} (m + 1)} \left(x + \frac {L}{2}\right),\tag{8}
$$

for beams of difraction orders m and $m + 1$ , respectively. Equating the z-coordinates yields the intersection coordinates:

$$
x = \frac {L}{2} \frac {(m + 1) k _ {z ; m} + m k _ {z ; m + 1}}{(m + 1) k _ {z ; m} - m k _ {z ; m + 1}},\tag{9}
$$

$$
z = \frac {L}{\kappa_ {x}} \frac {k _ {z ; m} k _ {z ; m + 1}}{(m + 1) k _ {z ; m} - m k _ {z ; m + 1}}.\tag{10}
$$

Figure 5 plots these boundary intersection coordinates calculated from Eqs. (9) and (10) for $L _ { x } = 2 0 \lambda$ Coordinates are normalized to L. Adjacent beams overlap below these intersection points and fully decouple above them. Hence, the first-mirror facets must be positioned at z-coordinates exceeding these critical thresholds.

The angular sector available for positioning the facet for order m is bounded by rays connecting the mask center to the nearest adjacent intersection points, shown as blue boundary lines in Fig. 6.

## 3 2D Two-Mirror Projection System

## 3.1 Design of the Two-Mirror Projection System

The development of the two-mirror projection system proceeds through an iterative design progression:

![](images/1a60c8584b167c2ceba28b60ab0765500c5305d9360fde92396d513128898474.jpg)  
Figure 5: Spatial intersection coordinates of adjacent beam boundaries (markers) computed via Eqs. (9) and (10) for $L _ { x } = 2 0 \lambda$ in the $x O z$ plane. Thin solid lines denote beam edges originating from the mask boundaries $( | x | = L / 2 , z = 0 )$ , the dashed line traces the intersection loci, and labels indicate difraction order pairs $( m , m + 1 )$ . Coordinates are normalized to mask width L.

![](images/aa426987df23bf27d76d93c26d26ea55edc1dced89bfc4b467ee5abf7d5cf22f.jpg)  
Figure 6: First-stage mirror system. Blue lines designate angular spatial-frequency sectors allocated to individual difraction harmonics.

Suggestions Design of the mirror system Discussion of disadvantages

This approach enables systematic iterative refinement of the two-mirror projection system.

Consider an illumination beam incident at $6 ^ { \circ }$ relative to the z-axis (the industrial standard for EUV lithography). The mask lateral dimension is $L = 1 0$ mm, the exposure wavelength is $\lambda = 1 1 . 2$ nm, and the mask pattern period is $L _ { x } = 8 \lambda / \sin { 6 ^ { \circ } } \approx 8 5 7$ nm. Under these conditions, the maximum propagating mask-order index is $M = \lfloor k _ { 0 } / \kappa _ { x } \rfloor = 7 6$ , and the maximum wafer-order index under 4× demagnification is $N = \lfloor M / 4 \rfloor = 1 9$

In the configurations evaluated below, the first mirror is located at $z = Z _ { 1 } = 1 0 0 0$ mm. The center of the m-th facet on the first mirror is located at $( \pm x _ { 1 } ^ { ( m ) } , Z _ { 1 } )$ , where $x _ { 1 } ^ { ( m ) } = Z _ { 1 }$ tan $\theta _ { m }$ and tan $\theta _ { m } = \kappa _ { x } m / k _ { z ; m }$

## 3.1.1 Example 1: Mask and Wafer Located on the Same Side of the Second Mirror

In this baseline geometry, the second mirror system is positioned below the wafer plane (mask and wafer are on the same side of it). The tilt angle of the m-th facet on the first mirror relative to the horizontal in this and the following example is $\alpha _ { 1 } ^ { ( m ) } = \theta _ { m } / 2$ . The center of the m-th facet on the second mirror is positioned at $( \pm x _ { 1 } ^ { ( m ) } , z _ { f } ^ { ( m ) } )$ , where $z _ { f } ^ { ( m ) } = Z _ { \mathrm { w } } - x _ { 1 } ^ { ( m ) } /$ tan $\theta _ { m } ^ { \mathrm { ( w ) } }$ with tan $\theta _ { m } ^ { \mathrm { ( w ) } } = 4 \kappa _ { x } m / k _ { z ; m } ^ { \mathrm { ( w ) } }$ . The tilt angle of the second-mirror facet relative to the horizontal is $\alpha _ { 2 } ^ { ( m ) } = \theta _ { m } ^ { ( \mathrm { w ) } } / 2$

Table 1 lists the structural parameters for the 19 positive-index transmitted orders.

Table 1: Mirror system configuration for Example 1 $( \lambda = 1 1 . 2$ nm, $L = 1 0$ mm, $L _ { x } = 8 5 7$ nm, $M = 7 6$ 2 N = 19, $Z _ { 1 } = 1 0 0 \dot { 0 }$ mm, $Z _ { \mathrm { w } } = - 3 0 0$ mm).

<table><tr><td>m</td><td> $\theta_m$  (°)</td><td> $\theta_m^{(w)}$  (°)</td><td> $x_1^{(m)}$  (mm)</td><td> $z_f^{(m)}$  (mm)</td><td> $a_m$  (mm)</td><td> $L_m^{(w)}$  (mm)</td><td> $\alpha_1^{(m)}$  (°)</td><td> $\alpha_2^{(m)}$  (°)</td></tr><tr><td>1</td><td>0.75</td><td>3.00</td><td>13.1</td><td>-549.7</td><td>10.00</td><td>10.01</td><td>0.37</td><td>1.50</td></tr><tr><td>2</td><td>1.50</td><td>6.00</td><td>26.1</td><td>-548.7</td><td>10.00</td><td>10.05</td><td>0.75</td><td>3.00</td></tr><tr><td>3</td><td>2.25</td><td>9.02</td><td>39.2</td><td>-547.1</td><td>9.99</td><td>10.12</td><td>1.12</td><td>4.51</td></tr><tr><td>4</td><td>3.00</td><td>12.07</td><td>52.3</td><td>-544.8</td><td>9.99</td><td>10.21</td><td>1.50</td><td>6.03</td></tr><tr><td>5</td><td>3.75</td><td>15.15</td><td>65.5</td><td>-541.8</td><td>9.98</td><td>10.34</td><td>1.87</td><td>7.57</td></tr><tr><td>6</td><td>4.50</td><td>18.28</td><td>78.6</td><td>-538.1</td><td>9.97</td><td>10.50</td><td>2.25</td><td>9.14</td></tr><tr><td>7</td><td>5.25</td><td>21.46</td><td>91.8</td><td>-533.6</td><td>9.96</td><td>10.70</td><td>2.62</td><td>10.73</td></tr><tr><td>8</td><td>6.00</td><td>24.72</td><td>105.1</td><td>-528.3</td><td>9.95</td><td>10.95</td><td>3.00</td><td>12.36</td></tr><tr><td>9</td><td>6.75</td><td>28.06</td><td>118.4</td><td>-522.2</td><td>9.93</td><td>11.25</td><td>3.38</td><td>14.03</td></tr><tr><td>10</td><td>7.51</td><td>31.51</td><td>131.8</td><td>-515.0</td><td>9.91</td><td>11.63</td><td>3.75</td><td>15.75</td></tr><tr><td>11</td><td>8.26</td><td>35.09</td><td>145.2</td><td>-506.7</td><td>9.90</td><td>12.09</td><td>4.13</td><td>17.55</td></tr><tr><td>12</td><td>9.02</td><td>38.84</td><td>158.8</td><td>-497.2</td><td>9.88</td><td>12.68</td><td>4.51</td><td>19.42</td></tr><tr><td>13</td><td>9.78</td><td>42.80</td><td>172.4</td><td>-486.1</td><td>9.85</td><td>13.43</td><td>4.89</td><td>21.40</td></tr><tr><td>14</td><td>10.54</td><td>47.03</td><td>186.1</td><td>-473.3</td><td>9.83</td><td>14.42</td><td>5.27</td><td>23.51</td></tr><tr><td>15</td><td>11.30</td><td>51.62</td><td>199.9</td><td>-458.3</td><td>9.81</td><td>15.80</td><td>5.65</td><td>25.81</td></tr><tr><td>16</td><td>12.07</td><td>56.74</td><td>213.8</td><td>-440.2</td><td>9.78</td><td>17.83</td><td>6.03</td><td>28.37</td></tr><tr><td>17</td><td>12.83</td><td>62.68</td><td>227.8</td><td>-417.7</td><td>9.75</td><td>21.25</td><td>6.42</td><td>31.34</td></tr><tr><td>18</td><td>13.60</td><td>70.18</td><td>242.0</td><td>-387.2</td><td>9.72</td><td>28.66</td><td>6.80</td><td>35.09</td></tr><tr><td>19</td><td>14.37</td><td>83.23</td><td>256.3</td><td>-330.4</td><td>9.69</td><td>82.13</td><td>7.19</td><td>41.61</td></tr></table>

The lateral span of the first mirror along the x-axis is $\pm 2 5 6 . 3$ mm at fixed height $z = Z _ { 1 } = 1 0 0 0$ mm, i.e., all facet centers of the first mirror lie in a single horizontal plane (facet tilt angles range from $0 . 3 7 ^ { \circ }$ to $7 . 1 9 ^ { \circ }$ visually indistinguishable from a flat mirror). The second mirror spans an identical lateral range, but its facets lie along a curved profile $z _ { f } ^ { ( m ) } = Z _ { \mathrm { w } } - x _ { 1 } ^ { ( \ r { m } ) } / \tan \theta _ { m } ^ { ( \mathrm { w } ) }$ with heights spanning $z _ { f } ^ { ( 1 ) } = - 5 4 9 . 7$ mm (center) to $z _ { f } ^ { ( 1 9 ) } = - 3 3 0 . 4 \mathrm { m m } ( \mathrm { e d g e } )$ . The maximum numerical aperture of the system reaches $\mathrm { N A } _ { \mathrm { m a x } } = \sin \theta _ { 1 9 } ^ { \mathrm { ( w ) } } = 0 . 9 9 3$ Figure 7 displays the ray-trace diagram in the developed projection system. Each m-th harmonic of the field scattered by the mask is converted by the first set of 2N planar facets into a beam parallel to the z-axis, and then focused onto the wafer at angle $\theta _ { m } ^ { \mathrm { ( w ) } }$ to the normal by the second set of 2N facets. The beam width $a _ { m } \approx 1 0$ mm is preserved upon first reflection (i.e., redirection into the −z direction), but after reflection from the second (tilted) mirror it projects onto the wafer with a footprint enlarged by a factor of $1 / \cos \theta _ { m } ^ { ( \mathrm { w } ) }$ For $m = 1 9 \ ( \theta _ { 1 9 } ^ { \mathrm { ( w ) } } = 8 3 . 2 ^ { \circ } )$ , the footprint reaches 82.1 mm. As the beam arrives at near-grazing incidence on the wafer, the perpendicular cross-section $a _ { m } = 9 . 7$ mm is stretched by a factor of 8.5.

Discussion. The analyzed system forms a demagnified pattern on the wafer via spatial harmonic transformation. The primary limitation of this design is that the wafer is situated within the ray convergence zone directed by the second mirror, severely restricting the physical clearance required for wafer stage manipulation and handling — a critical constraint in industrial lithography. Furthermore, the $m = 0$ beam is omitted from the field arriving at the wafer, and high-order beams produce relatively large footprints on the wafer plane. The latter two aspects are secondary compared to the first constraint.

Suggestion 1. Position the wafer outside the space between the first and second mirrors.

![](images/6c8e249df936ef1db7421e34d4b4d79a05f1abd0f2b413611b0fee30bc45f430.jpg)  
Figure 7: Ray tracing in the all-reflective two-mirror projection system for $N = 1 9$ orders (showing orders $m = 1 , 4 , 7 , 1 0 , 1 3 , 1 6 , 1 9 )$ . Color represents difraction order: purple denotes $m = 1 ~ ( \theta _ { m } ^ { ( \mathrm { w ) } } = 3 . 0 ^ { \circ } )$ , dark red denotes $m = 1 9 \ ( \theta _ { m } ^ { ( \mathrm { w ) } } = 8 3 . 2 ^ { \circ } )$ . Solid lines show marginal rays from the mask edges $\pm L / 2$ . Dashed lines show axial rays. Rays trace from the mask $( z = 0 )$ through mirror $1 ~ ( z = 1 0 0 0 ~ \mathrm { \bar { m m } ) }$ and mirror 2 $( z \in [ - 5 5 0 , - 3 3 0 ]$ mm) to the wafer $( z = - 3 0 0 ~ \mathrm { m m } )$ ).

## 3.1.2 Example 2: Wafer Positioned Below the Second Mirror

We now consider a configuration in which the second mirror system is positioned between the mask and the wafer, placing the wafer entirely below the second mirror (mask and wafer are on opposite sides of it). The first mirror remains identical $( z = Z _ { 1 } = 1 0 0 0 \ \mathrm { m m } )$ . The vertically descending beams are reflected by the second mirror toward the center of the wafer while continuing downward. The center of the m-th facet of the second mirror is positioned at $( \pm x _ { 1 } ^ { ( m ) } , z _ { f } ^ { ( m ) } )$ , where

$$
z _ {f} ^ {(m)} = Z _ {\mathrm{w}} + \frac {x _ {1} ^ {(m)}}{\tan \theta_ {m} ^ {(\mathrm{w})}},\tag{11}
$$

so that the second mirror system spans the domain from $z _ { f } ^ { ( 1 ) } = - 5 0 . 3$ mm (center) to $z _ { f } ^ { ( 1 9 ) } = - 2 6 9 . 6$ mm (edge). The height diference (219 mm) is identical to that in Example 1, but the second mirror system is now positioned above the wafer. The facet tilt angle relative to the horizontal is $\alpha _ { 2 } ^ { ( m ) } = 9 0 ^ { \circ } - \theta _ { m } ^ { \mathrm { ( w ) } } / 2 \colon$ the facets are nearly vertical, and beams strike them at grazing angles $\theta _ { m } ^ { \mathrm { ( w ) } } / 2$ measured from the facet plane (from $1 . 5 ^ { \circ }$ for m = 1 to $4 1 . 6 ^ { \circ }$ for $m = 1 9 )$ , corresponding to incidence angles $9 0 ^ { \circ } - \theta _ { m } ^ { \mathrm { ( w ) } } / 2$ from the facet normal.

Table 2 details the mirror configurations for the 19 positive-index orders. The final column $\ell _ { 2 } ^ { ( m ) }$ defines the minimum facet length required to intercept the full beam width $a _ { m }$ at grazing incidence: $\ell _ { 2 } ^ { ( m ) } =$ $a _ { m } / \sin \Bigl ( \theta _ { m } ^ { ( \mathrm { w } ) } / 2 \Bigr )$ . The ray trace is shown in Fig. 8.  
Table 2: Mirror system parameters for the configuration with the wafer below the second mirror $( \lambda = 1 1 . 2 \mathrm { n m }$ $L = 1 0$ mm, $L _ { x } = 8 5 7$ nm, M = 76, N = 19, $\bar { Z _ { 1 } } = 1 0 0 0$ mm, $Z _ { \mathrm { w } } = - 3 0 0$ mm).

<table><tr><td>m</td><td> $\theta_m$  (°)</td><td> $\theta_m^{(w)}$  (°)</td><td> $x_1^{(m)}$  (mm)</td><td> $z_f^{(m)}$  (mm)</td><td> $a_m$  (mm)</td><td> $L_m^{(w)}$  (mm)</td><td> $\alpha_1^{(m)}$  (°)</td><td> $\alpha_2^{(m)}$  (°)</td><td> $\ell_2^{(m)}$  (mm)</td></tr><tr><td>1</td><td>0.75</td><td>3.00</td><td>13.1</td><td>-50.3</td><td>10.00</td><td>10.01</td><td>0.37</td><td>88.50</td><td>382.5</td></tr><tr><td>2</td><td>1.50</td><td>6.00</td><td>26.1</td><td>-51.3</td><td>10.00</td><td>10.05</td><td>0.75</td><td>87.00</td><td>191.0</td></tr><tr><td>3</td><td>2.25</td><td>9.02</td><td>39.2</td><td>-52.9</td><td>9.99</td><td>10.12</td><td>1.12</td><td>85.49</td><td>127.1</td></tr><tr><td>4</td><td>3.00</td><td>12.07</td><td>52.3</td><td>-55.2</td><td>9.99</td><td>10.21</td><td>1.50</td><td>83.97</td><td>95.0</td></tr><tr><td>5</td><td>3.75</td><td>15.15</td><td>65.5</td><td>-58.2</td><td>9.98</td><td>10.34</td><td>1.87</td><td>82.43</td><td>75.7</td></tr><tr><td>6</td><td>4.50</td><td>18.28</td><td>78.6</td><td>-61.9</td><td>9.97</td><td>10.50</td><td>2.25</td><td>80.86</td><td>62.8</td></tr><tr><td>7</td><td>5.25</td><td>21.46</td><td>91.8</td><td>-66.4</td><td>9.96</td><td>10.70</td><td>2.62</td><td>79.27</td><td>53.5</td></tr><tr><td>8</td><td>6.00</td><td>24.72</td><td>105.1</td><td>-71.7</td><td>9.95</td><td>10.95</td><td>3.00</td><td>77.64</td><td>46.5</td></tr><tr><td>9</td><td>6.75</td><td>28.06</td><td>118.4</td><td>-77.8</td><td>9.93</td><td>11.25</td><td>3.38</td><td>75.97</td><td>41.0</td></tr><tr><td>10</td><td>7.51</td><td>31.51</td><td>131.8</td><td>-85.0</td><td>9.91</td><td>11.63</td><td>3.75</td><td>74.25</td><td>36.5</td></tr><tr><td>11</td><td>8.26</td><td>35.09</td><td>145.2</td><td>-93.3</td><td>9.90</td><td>12.09</td><td>4.13</td><td>72.45</td><td>32.8</td></tr><tr><td>12</td><td>9.02</td><td>38.84</td><td>158.8</td><td>-102.8</td><td>9.88</td><td>12.68</td><td>4.51</td><td>70.58</td><td>29.7</td></tr><tr><td>13</td><td>9.78</td><td>42.80</td><td>172.4</td><td>-113.9</td><td>9.85</td><td>13.43</td><td>4.89</td><td>68.60</td><td>27.0</td></tr><tr><td>14</td><td>10.54</td><td>47.03</td><td>186.1</td><td>-126.7</td><td>9.83</td><td>14.42</td><td>5.27</td><td>66.49</td><td>24.6</td></tr><tr><td>15</td><td>11.30</td><td>51.62</td><td>199.9</td><td>-141.7</td><td>9.81</td><td>15.80</td><td>5.65</td><td>64.19</td><td>22.5</td></tr><tr><td>16</td><td>12.07</td><td>56.74</td><td>213.8</td><td>-159.8</td><td>9.78</td><td>17.83</td><td>6.03</td><td>61.63</td><td>20.6</td></tr><tr><td>17</td><td>12.83</td><td>62.68</td><td>227.8</td><td>-182.3</td><td>9.75</td><td>21.25</td><td>6.42</td><td>58.66</td><td>18.7</td></tr><tr><td>18</td><td>13.60</td><td>70.18</td><td>242.0</td><td>-212.8</td><td>9.72</td><td>28.66</td><td>6.80</td><td>54.91</td><td>16.9</td></tr><tr><td>19</td><td>14.37</td><td>83.23</td><td>256.3</td><td>-269.6</td><td>9.69</td><td>82.13</td><td>7.19</td><td>48.39</td><td>14.6</td></tr></table>

Discussion. The lateral span of the mirrors along the x-axis (±256.3 mm) and the maximum numerical aperture $\mathrm { N A } _ { \mathrm { m a x } } = 0 . 9 9 3$ remain identical to Example 1. The beam widths $a _ { m }$ and footprint dimensions $L _ { m } ^ { \mathrm { ( w ) } }$ on the wafer are unchanged. The key diference of this configuration is grazing incidence on the second mirror. At suficiently small grazing angles, a suitable material can provide useful total-external-reflection reflectance without a Bragg stack. The critical angle and absorption depend on the material and wavelength and must be evaluated from the complex refractive index. No universal $1 5 ^ { \circ }$ threshold is assumed. At larger grazing angles, multilayer coatings require optimization for the actual incidence angle. The total optical path length of the central ray from the mask to the wafer increases from 2300.4 mm $( m = 1 )$ to 2560.0 mm $( m = 1 9 )$ corresponding to an optical path diference of ≈ 260 mm.

The minimum facet length $\ell _ { 2 } ^ { ( m ) } = a _ { m } / \sin \left( \theta _ { m } ^ { ( \mathrm { w } ) } / 2 \right)$ is large for low difraction orders, reaching 382.5 mm for $m = 1$ , 191.0 mm for $m = 2 .$ , and 127.1 mm for ${ \dot { m } } = 3$ . This follows from the grazing-incidence footprint enlargement by $1 / \sin \left( \theta _ { m } ^ { \mathrm { ( w ) } } / 2 \right)$

Suggestion 2. To obtain more compact second-mirror facets, place the wafer in the base plane of the first mirror and the mask in the base plane of the second. Furthermore, this layout restores the $m = 0$ beam to the field reaching the wafer.

## 3.1.3 Example 3: Wafer in the Plane of Mirror 1, Mask in the Base Plane of Mirror 2

In this example, the wafer is placed in the plane of the first mirror $( z = Z _ { 1 } = 1 0 0 0 \ \mathrm { m m } )$ and the mask is located at the base of the second $( z = 0 )$ . The second mirror consists of a system of facets distributed in height: central facets (small m) reside near the mask, while peripheral facets (large m) ascend toward the

wafer

![](images/07e8a3f4b42bdbc028fda7056f9da3ad25349abb1e05f579001884cf9dbb8758.jpg)  
Figure 8: Ray tracing in the configuration with the wafer below the second mirror $( N = 1 9$ , showing orders $m { \overset { \cdot } { = } } 1 , 4 , 7 , 1 0 , 1 3 , 1 6 , 1 9 )$ . The second mirror system is positioned between the mask $( z = 0 )$ and wafer $( z = - 3 0 0 \ \mathrm { m m } )$ . Its facets are nearly vertical (tilt relative to the horizontal $9 0 ^ { \circ } - \theta _ { m } ^ { \mathrm { ( w ) } } / 2 )$ and plotted with full length $\ell _ { 2 } ^ { ( m ) } = a _ { m } / \sin \left( \theta _ { m } ^ { ( \mathrm { w } ) } / 2 \right)$ required to intercept the entire beam (up to 382.5 mm for $m = 1 )$ .

wafer. The spatial distance from the wafer center to the central facets of the second mirror is on the order of the mask–wafer distance $Z _ { 1 } = 1 0 0 0$ mm. Figure 9 shows the ray trace for this projection system.

First mirror at $z = Z _ { 1 }$ : facet m is centered at $( \pm x _ { 1 } ^ { ( m ) } , Z _ { 1 } ) , x _ { 1 } ^ { ( m ) } = Z _ { 1 }$ tan $\theta _ { m }$ . Unlike Example 1, the first mirror does not collimate the beams vertically, but deflects them downward and outward:

$$
\left(\sin \theta_ {m}, \cos \theta_ {m}\right) \longrightarrow \left[ \sin \left(\theta_ {m} ^ {\mathrm{(w)}} - \theta_ {m}\right), - \cos \left(\theta_ {m} ^ {\mathrm{(w)}} - \theta_ {m}\right) \right].\tag{12}
$$

The angle of incidence on the first mirror is $i _ { 1 } ^ { ( m ) } = \theta _ { m } ^ { ( \mathrm { w } ) } / 2 ( 1 . 5 ^ { \circ } - 4 1 . 6 ^ { \circ } )$ , and the facet tilt is $\alpha _ { 1 } ^ { ( m ) } = \theta _ { m } ^ { ( \mathrm { w ) } } / 2 - \theta _ { m }$ $( 0 . 8 ^ { \circ } - 2 7 . 2 ^ { \circ }$ relative to the horizontal).

Second mirror: facet m is centered at $( \pm x _ { f } ^ { ( m ) } , z _ { f } ^ { ( m ) } )$ , where

$$
z _ {f} ^ {(m)} = Z _ {1} - \frac {Z _ {1} \tan \theta_ {m}}{\tan \theta_ {m} ^ {\mathrm{(w)}} - \tan \left(\theta_ {m} ^ {\mathrm{(w)}} - \theta_ {m}\right)}, \qquad x _ {f} ^ {(m)} = (Z _ {1} - z _ {f} ^ {(m)}) \tan \theta_ {m} ^ {\mathrm{(w)}}.\tag{13}
$$

For small $m$ , tan $\theta _ { m } \ll$ tan $\theta _ { m } ^ { \mathrm { ( w ) } }$ , yielding $z _ { f } ^ { ( m ) } \approx 0$ — central facets lie near the mask. For $m = 1 9$ 2 $z _ { f } \approx 9 5 6$ mm — the facet is near the wafer. The second mirror redirects the beam toward the center of the wafer:

$$
\left[ \pm \sin \left(\theta_ {m} ^ {\mathrm{(w)}} - \theta_ {m}\right), - \cos \left(\theta_ {m} ^ {\mathrm{(w)}} - \theta_ {m}\right) \right] \longrightarrow \left[ \mp \sin \theta_ {m} ^ {\mathrm{(w)}}, \cos \theta_ {m} ^ {\mathrm{(w)}} \right].\tag{14}
$$

The angle of incidence on the second mirror is $i _ { 2 } ^ { ( m ) } = \theta _ { m } / 2 \left( 0 . 4 ^ { \circ } - 7 . 2 ^ { \circ } \right)$ , and facet tilt angles are $\alpha _ { 2 } ^ { ( m ) } \ : ( 2 . 6 ^ { \circ } - 7 6 . 0 ^ { \circ }$ relative to the horizontal). The facet lengths of the second mirror are compact: $\ell _ { 2 } ^ { ( m ) } = a _ { m } / \cos ( \theta _ { m } / 2 )$ ≈ 10 mm. Geometric configurations for all facets $m = 1 { - } 1 9$ are listed in Table 3.  
Table 3: Mirror system configuration with the wafer in the plane of the first mirror $( i _ { 1 }$ and $i _ { 2 }$ are angles of incidence on the first and second mirrors, respectively, $P _ { m }$ is total optical path length).

<table><tr><td>m</td><td> $\theta_m$  (°)</td><td> $\theta_m^{(w)}$  (°)</td><td> $x_1^{(m)}$  (mm)</td><td> $x_f^{(m)}$  (mm)</td><td> $z_f^{(m)}$  (mm)</td><td> $i_1^{(m)}$  (°)</td><td> $i_2^{(m)}$  (°)</td><td> $\ell_2^{(m)}$  (mm)</td><td> $P_m$  (mm)</td></tr><tr><td>1</td><td>0.75</td><td>3.00</td><td>13.1</td><td>52.2</td><td>2.0</td><td>1.50</td><td>0.37</td><td>10.0</td><td>2998.1</td></tr><tr><td>2</td><td>1.50</td><td>6.00</td><td>26.1</td><td>104.2</td><td>8.2</td><td>3.00</td><td>0.75</td><td>10.0</td><td>2992.5</td></tr><tr><td>3</td><td>2.25</td><td>9.02</td><td>39.2</td><td>155.8</td><td>18.5</td><td>4.51</td><td>1.12</td><td>10.0</td><td>2982.9</td></tr><tr><td>4</td><td>3.00</td><td>12.07</td><td>52.3</td><td>206.7</td><td>33.0</td><td>6.03</td><td>1.50</td><td>10.0</td><td>2969.5</td></tr><tr><td>5</td><td>3.75</td><td>15.15</td><td>65.5</td><td>256.7</td><td>51.8</td><td>7.57</td><td>1.87</td><td>10.0</td><td>2951.8</td></tr><tr><td>6</td><td>4.50</td><td>18.28</td><td>78.6</td><td>305.5</td><td>74.9</td><td>9.14</td><td>2.25</td><td>10.0</td><td>2929.8</td></tr><tr><td>7</td><td>5.25</td><td>21.46</td><td>91.8</td><td>352.8</td><td>102.6</td><td>10.73</td><td>2.62</td><td>10.0</td><td>2903.1</td></tr><tr><td>8</td><td>6.00</td><td>24.72</td><td>105.1</td><td>398.2</td><td>134.9</td><td>12.36</td><td>3.00</td><td>10.0</td><td>2871.2</td></tr><tr><td>9</td><td>6.75</td><td>28.06</td><td>118.4</td><td>441.3</td><td>172.1</td><td>14.03</td><td>3.38</td><td>9.9</td><td>2833.8</td></tr><tr><td>10</td><td>7.51</td><td>31.51</td><td>131.8</td><td>481.6</td><td>214.4</td><td>15.75</td><td>3.75</td><td>9.9</td><td>2790.0</td></tr><tr><td>11</td><td>8.26</td><td>35.09</td><td>145.2</td><td>518.4</td><td>262.2</td><td>17.55</td><td>4.13</td><td>9.9</td><td>2739.0</td></tr><tr><td>12</td><td>9.02</td><td>38.84</td><td>158.8</td><td>550.9</td><td>315.8</td><td>19.42</td><td>4.51</td><td>9.9</td><td>2679.6</td></tr><tr><td>13</td><td>9.78</td><td>42.80</td><td>172.4</td><td>578.1</td><td>375.7</td><td>21.40</td><td>4.89</td><td>9.9</td><td>2610.1</td></tr><tr><td>14</td><td>10.54</td><td>47.03</td><td>186.1</td><td>598.4</td><td>442.6</td><td>23.51</td><td>5.27</td><td>9.9</td><td>2528.3</td></tr><tr><td>15</td><td>11.30</td><td>51.62</td><td>199.9</td><td>609.5</td><td>517.3</td><td>25.81</td><td>5.65</td><td>9.9</td><td>2430.4</td></tr><tr><td>16</td><td>12.07</td><td>56.74</td><td>213.8</td><td>608.1</td><td>601.2</td><td>28.37</td><td>6.03</td><td>9.8</td><td>2310.5</td></tr><tr><td>17</td><td>12.83</td><td>62.68</td><td>227.8</td><td>587.6</td><td>696.5</td><td>31.34</td><td>6.42</td><td>9.8</td><td>2157.6</td></tr><tr><td>18</td><td>13.60</td><td>70.18</td><td>242.0</td><td>533.1</td><td>807.8</td><td>35.09</td><td>6.80</td><td>9.8</td><td>1944.5</td></tr><tr><td>19</td><td>14.37</td><td>83.23</td><td>256.3</td><td>369.8</td><td>956.1</td><td>41.61</td><td>7.19</td><td>9.8</td><td>1526.5</td></tr></table>

![](images/02ac3c6bb8cf8d22f54dbc2eb0348e7c088c156a4097c30998d0919264bed582.jpg)  
Figure 9: Ray tracing with the wafer in the plane of the first mirror and the mask at the base of the second $( N = 1 9$ , showing orders $m = 1 , 4 , 7 , 1 0 , 1 3 , 1 6 , 1 9 )$ . The beam from the mask $( z = 0 )$ propagates upward to mirror 1 $( z = 1 0 0 0 \ \mathrm { m m } )$ , reflects downward and outward at angle $( \theta _ { m } ^ { \mathrm { ( w ) } } - \theta _ { m } )$ , intercepts the second mirror facet $\left( z _ { f } \right.$ from 2 mm to 956 mm), which directs the beam upward to the center of the wafer $\left( z = Z _ { 1 } \right)$ at convergence angle $\theta _ { m } ^ { \mathrm { ( w ) } }$

Discussion. The optical path length decreases with order index: from 2998 mm $( m = 1 )$ to 1527 mm $( m = 1 9 )$ , creating an optical path diference of 1472 mm.

Suggestion 3. Position the facets of the second mirror such that the optical path lengths across all difraction orders are identical.

## 3.1.4 Example 4: Equal Optical Path Length, NA ∼ 1

In Example $^ { 3 , }$ optical path lengths $P _ { m }$ vary substantially across orders (from 2998 mm for $m = 1$ to 1527 mm for $m = 1 9 )$ , which introduces order-dependent propagation phase shifts even under coherent monochromatic illumination. In this example, the facet coordinates of the first mirror are preserved as in Example 3 (z<sub>1</sub> = Z<sub>1</sub> = const, $x _ { 1 } ^ { ( m ) } = Z _ { 1 }$ tan $\theta _ { m } )$ , while the facet heights $z _ { f } ^ { ( m ) }$ of the second mirror and the first-mirror deflection angles $\beta _ { m }$ are adjusted so that the total optical path length $P _ { m }$ is identical for all difraction orders (excluding $m = 0 )$ . The maximum positive order index is $N = 1 9$ , and $\mathrm { N A } _ { \mathrm { m a x } } = 0 . 9 9 3$ , as in Example 3.

The second mirror redirects each beam toward the center of the wafer $( 0 , Z _ { 1 } )$ at angle $\theta _ { m } ^ { \mathrm { ( w ) } }$ . The lateral coordinate is $x _ { f } ^ { ( m ) } = ( Z _ { 1 } - z _ { f } ^ { ( m ) } )$ tan $\theta _ { m } ^ { \mathrm { ( w ) } }$ . The first mirror reflects the beam at a variable angle $\beta _ { m }$ (from $2 . 2 ^ { \circ }$ for $m = 1$ to 81.2<sup>◦</sup> for $m = 1 9 )$ , determined by the position of the corresponding facet of the second mirror:

$$
\tan \beta_ {m} = \frac {x _ {f} ^ {(m)} - x _ {1} ^ {(m)}}{Z _ {1} - z _ {f} ^ {(m)}}.\tag{15}
$$

The total optical path length is:

$$
P _ {m} = \frac {Z _ {1}}{\cos \theta_ {m}} + \left[ \left(x _ {f} ^ {(m)} - x _ {1} ^ {(m)}\right) ^ {2} + \left(Z _ {1} - z _ {f} ^ {(m)}\right) ^ {2} \right] ^ {1 / 2} + \frac {Z _ {1} - z _ {f} ^ {(m)}}{\cos \theta_ {m} ^ {\mathrm{(w)}}}.\tag{16}
$$

Here, the first term represents the path from the mask to the first mirror (fixed height $Z _ { 1 } ,$ but varying cos $\theta _ { m }$ due to difering $k _ { z ; m } )$ . The second term is the path from the first to the second mirror. The third term is the path from the second mirror to the wafer. The parameter $u _ { m } = Z _ { 1 } - z _ { f } ^ { ( m ) }$ is determined via bisection for each order m to enforce $P _ { m } \approx 2 9 9 8 . 1$ mm. As a result, $\Delta P = P _ { \mathrm { m a x } } - P _ { \mathrm { m i n } } = 0$ (within numerical precision), removing order-dependent propagation phase shifts. Phase diferences introduced by the mask and coatings remain. For a source with finite bandwidth, temporal coherence requires a separate assessment.

Table 4: Configuration of the equal-path mirror system $( N = 1 9 , \mathrm { { N A } = 0 . 9 9 3 ) }$ . Here $\beta$ is the reflection angle from mirror $1 , i _ { 1 }$ and $i _ { 2 }$ are angles of incidence, $\ell _ { 2 }$ is the facet length of mirror 2, and $P _ { m }$ is the total optical path length.

<table><tr><td>m</td><td> $\theta_{m}^{(w)}$  (°)</td><td> $z_{f}$  (mm)</td><td> $x_{f}$  (mm)</td><td> $\beta$  (°)</td><td> $i_{1}$  (°)</td><td> $i_{2}$  (°)</td><td> $\ell_{2}$  (mm)</td><td> $P_{m}$  (mm)</td></tr><tr><td>1</td><td>3.00</td><td>2.0</td><td>52.2</td><td>2.2</td><td>1.50</td><td>0.37</td><td>10.0</td><td>2998.1</td></tr><tr><td>2</td><td>6.00</td><td>5.4</td><td>104.5</td><td>4.5</td><td>3.00</td><td>0.75</td><td>10.0</td><td>2998.1</td></tr><tr><td>3</td><td>9.02</td><td>11.0</td><td>157.0</td><td>6.8</td><td>4.52</td><td>1.11</td><td>10.0</td><td>2998.1</td></tr><tr><td>4</td><td>12.07</td><td>19.0</td><td>209.7</td><td>9.1</td><td>6.06</td><td>1.48</td><td>10.0</td><td>2998.1</td></tr><tr><td>5</td><td>15.15</td><td>29.4</td><td>262.8</td><td>11.5</td><td>7.62</td><td>1.83</td><td>10.0</td><td>2998.1</td></tr><tr><td>6</td><td>18.28</td><td>42.4</td><td>316.2</td><td>13.9</td><td>9.22</td><td>2.17</td><td>10.0</td><td>2998.1</td></tr><tr><td>7</td><td>21.46</td><td>58.3</td><td>370.2</td><td>16.5</td><td>10.86</td><td>2.50</td><td>10.0</td><td>2998.1</td></tr><tr><td>8</td><td>24.72</td><td>77.1</td><td>424.8</td><td>19.1</td><td>12.55</td><td>2.80</td><td>10.0</td><td>2998.1</td></tr><tr><td>9</td><td>28.06</td><td>99.4</td><td>480.1</td><td>21.9</td><td>14.32</td><td>3.09</td><td>9.9</td><td>2998.1</td></tr><tr><td>10</td><td>31.51</td><td>125.4</td><td>536.2</td><td>24.8</td><td>16.16</td><td>3.35</td><td>9.9</td><td>2998.1</td></tr><tr><td>11</td><td>35.09</td><td>155.7</td><td>593.2</td><td>28.0</td><td>18.11</td><td>3.57</td><td>9.9</td><td>2998.1</td></tr><tr><td>12</td><td>38.84</td><td>191.1</td><td>651.3</td><td>31.3</td><td>20.18</td><td>3.75</td><td>9.9</td><td>2998.1</td></tr><tr><td>13</td><td>42.80</td><td>232.5</td><td>710.7</td><td>35.0</td><td>22.41</td><td>3.88</td><td>9.9</td><td>2998.1</td></tr><tr><td>14</td><td>47.03</td><td>281.4</td><td>771.4</td><td>39.2</td><td>24.85</td><td>3.93</td><td>9.9</td><td>2998.1</td></tr><tr><td>15</td><td>51.62</td><td>339.9</td><td>833.6</td><td>43.8</td><td>27.57</td><td>3.90</td><td>9.8</td><td>2998.1</td></tr><tr><td>16</td><td>56.74</td><td>411.4</td><td>897.5</td><td>49.3</td><td>30.67</td><td>3.73</td><td>9.8</td><td>2998.1</td></tr><tr><td>17</td><td>62.68</td><td>502.4</td><td>963.5</td><td>55.9</td><td>34.38</td><td>3.38</td><td>9.8</td><td>2998.1</td></tr><tr><td>18</td><td>70.18</td><td>628.2</td><td>1031.6</td><td>64.8</td><td>39.19</td><td>2.70</td><td>9.7</td><td>2998.1</td></tr><tr><td>19</td><td>83.23</td><td>869.1</td><td>1102.1</td><td>81.2</td><td>47.79</td><td>1.01</td><td>9.7</td><td>2998.1</td></tr></table>

The angles of incidence on the first mirror, $i _ { 1 } = ( \theta _ { m } + \beta _ { m } ) / 2$ , vary from $1 . 5 ^ { \circ }$ to $4 7 . 8 ^ { \circ }$ . On the second mirror, $i _ { 2 }$ varies from $0 . 4 ^ { \circ }$ to $3 . 9 ^ { \circ }$ , which is substantially smaller than $\dot { i } _ { 2 } = \theta _ { m } / 2 \ ( 0 . 4 ^ { \circ } - 7 . 2 ^ { \circ } )$ in Example $^ { 3 , }$ since adjusting $\beta _ { m }$ reduces the incidence angle on the second mirror for high orders. Facet lengths are $\ell _ { 2 } \approx 1 0$ mm. Figure 10 shows the ray trace of the proposed equal-path projection system.

![](images/8ec0f096a5ac1054d3ff0ef4a0b4e41d37e6d67155d0acc0baf2803194208d74.jpg)  
Figure 10: Ray tracing in the equal-path projection system $( N = 1 9 , \mathrm { N A } = 0 . 9 9 3$ , showing orders $m =$ $1 , \bar { 4 } , 7 , 1 0 , 1 3 , 1 \bar { 6 } , 1 9 )$ . The first mirror lies in the plane $z = Z _ { 1 } = 1 0 0 0$ mm. The deflection angle $\beta _ { m }$ varies from $2 . 2 ^ { \circ }$ to 81.2<sup>◦</sup>. The second mirror is profiled such that total optical path length $P _ { m } \approx 2 9 9 8 . 1$ mm across all orders.

## 3.2 Bragg Coatings of Mirror Facets for Example 4

Each of the $2 N = 3 8$ facets of the first and second mirrors in Example 4 operates at its own specific angle of incidence. Specifically, the angle of incidence on the first mirror $i _ { 1 } ^ { ( m ) }$ ranges from $1 . 5 0 ^ { \circ } ~ ( m = 1 )$ to $4 7 . 7 9 ^ { \circ }$ $( m = 1 9 )$ , while $i _ { 2 } ^ { ( m ) }$ on the second mirror ranges from $0 . 3 7 ^ { \circ }$ to $3 . 9 3 ^ { \circ }$ (see Tables 5 and 6, column $\theta _ { \mathrm { i n c } } )$ . A standard $\mathrm { M o } / \mathrm { S i }$ Bragg coating (40–50 bilayers) provides maximum reflectance near a single fixed design angle. A single uniform coating cannot maintain high reflectance across the entire $0 . 4 ^ { \circ } { - } 4 7 . 8 ^ { \circ }$ angular range. Therefore, individually optimized Bragg coatings maximizing reflectance at the exact operational angle of incidence must be designed for each facet.

## 3.2.1 Formulation of the Facet Bragg Optimization Problem

For each facet specified by mirror index $j \in \{ 1 , 2 \}$ and difraction order $m \in \{ 1 , \ldots , 1 9 \}$ , a target angle of incidence $\theta _ { \mathrm { t a r g e t } } = i _ { j } ^ { ( m ) }$ (measured from the facet normal) is assigned. We seek to determine the layer thicknesses $d _ { 1 }$ (absorbing material) and $d _ { 2 }$ (spacer material) of a periodic Bragg mirror comprising $N _ { b } = 3 0$ bilayers $( \mathrm { i . e . , 2 } \dot { N } _ { b } = 6 0 $ individual layers total) that maximize the reflectance $R = | r | ^ { 2 }$ at incident angle $\theta _ { \mathrm { t a r g e t } } { \mathrm { : } }$

$$
(d _ {1} ^ {*}, d _ {2} ^ {*}) = \arg \max _ {d _ {1}, d _ {2}} R (d _ {1}, d _ {2}; \theta_ {\mathrm{target}}).\tag{17}
$$

Here, $r = r ( d _ { 1 } , d _ { 2 } ; \theta )$ is the complex field reflection coeficient calculated via the transfer-matrix method (TMM) for TE polarization. The multilayer structure is: vacuum / layer $1 ( d _ { 1 } ) ~ /$ layer $2 ( d _ { 2 } ) / \ldots /$ layer $1 ( d _ { 1 } )$ / layer $2 ( d _ { 2 } ) \ _ { I }$ / vacuum (60 layers total, bounded by vacuum with $\varepsilon = 1$ on both sides). Optical constants $( \varepsilon = ( 1 - \overset { \cdot } { \delta } - \overset { \cdot } { \mathrm { i } } \beta ) ^ { 2 }$ , where δ is the refractive index decrement and $\beta$ is the absorption index) are obtained from tabulated reference data [18, 19].

Transfer-matrix method (TMM). At incidence angle θ, layer i has longitudinal wavenumber $k _ { z } ^ { \left( i \right) } =$ $k _ { 0 } ( \varepsilon _ { i } - \sin ^ { 2 } \theta ) ^ { 1 / 2 }$ and TE admittance $p _ { i } = k _ { z } ^ { ( i ) } / k _ { 0 }$ . The Fresnel coeficients are $r _ { i j } = ( p _ { i } - p _ { j } ) / ( p _ { i } + p _ { j } )$ and $t _ { i j } = 2 p _ { i } / ( p _ { i } + p _ { j } )$ . Define the entering-interface matrix and the propagation matrix of layer i by

$$
\begin{array}{r l} & {\mathbf {D} _ {i - 1, i} = \frac {1}{t _ {i - 1 , i}} \left( \begin{array}{c c} 1 & r _ {i - 1, i} \\ r _ {i - 1, i} & 1 \end{array} \right),} \\ & {\quad \mathbf {P} _ {i} = \mathrm{diag} (\mathrm{e} ^ {\mathrm{i} \phi_ {i}}, \mathrm{e} ^ {- \mathrm{i} \phi_ {i}}), \qquad \phi_ {i} = k _ {z} ^ {(i)} d _ {i},} \\ & {\quad \mathbf {M} = \mathbf {D} _ {0, 1} \mathbf {P} _ {1} \mathbf {D} _ {1, 2} \mathbf {P} _ {2} \dots \mathbf {D} _ {5 9, 6 0} \mathbf {P} _ {6 0} \mathbf {D} _ {6 0, \mathrm{sub}}.} \end{array}\tag{18}
$$

Here medium 0 and the substrate are vacuum. The matrices are multiplied in the written order, mapping substrate amplitudes to entrance amplitudes. The complex reflection coeficient is $r = M _ { 2 1 } / M _ { 1 1 }$ and $R \stackrel { \cdot } { = } | r | ^ { \frac { \bigtriangledown } { 2 } }$ Optimization algorithm. The objective function ${ f ( d _ { 1 } , d _ { 2 } ) = - R ( d _ { 1 } , d _ { 2 } ; \theta _ { \mathrm { t a r g e t } } ) }$ is minimized via a two-stage procedure:

1. Local optimization using the Nelder–Mead simplex algorithm, initialized near the first-order Bragg condition: $\begin{array} { r } { d _ { 1 } \operatorname { R e } \left( \varepsilon _ { 1 } - \sin ^ { 2 } \theta \right) ^ { 1 / 2 } + d _ { 2 } \operatorname { R e } \left( \varepsilon _ { 2 } - \sin ^ { 2 } \theta \right) ^ { 1 / 2 } = \lambda / 2 . } \end{array}$

2. Global optimization using the diferential evolution algorithm (differential\_evolution in SciPy, population-size multiplier popsize=15 (30 candidates for two variables), up to 80 iterations) within bounds $d _ { 1 } \in [ 0 . 3 , 5 ]$ nm, $d _ { 2 } \in [ 0 . 3 , 9 ]$ nm, followed by quasi-Newton refinement using the $\mathrm { L } { \mathrm { - } } \mathrm { B F G S { - } B }$ method.

The parameters yielding the highest R for the target angle are retained.

## 3.2.2 Configuration 1: λ = 13.5 nm, Mo/Si

The absorbing material is Mo $( \delta = 0 . 0 7 6 3 , \beta = 0 . 0 0 6 4 )$ and the spacer is Si $( \delta = 0 . 0 0 1 0 , \beta = 0 . 0 0 1 8 )$ . To retain the angles and numerical aperture of Example 4 at this wavelength, the mask period is scaled in proportion to λ, giving $L _ { x } = 8 \lambda /$ sin $6 ^ { \circ } \approx 1 0 3 3 . 2$ nm. At fixed $L _ { x } \approx 8 5 7$ nm the maximum wafer index would instead be $N = 1 5$ . Optimization results for the 38 tabulated facets are summarized in Table 5.

Table 5: Layer thicknesses of optimized Bragg mirrors for Example 4 (λ = 13.5 nm, Mo/Si, 60 layers, TE polarization). $d _ { \mathrm { M o } }$ and $d _ { \mathrm { S i } }$ are layer thicknesses, r is complex field reflection coeficient, $R = | r | ^ { 2 }$ is power reflectance at target incidence angle $\theta _ { \mathrm { i n c } }$

<table><tr><td>Mirror</td><td>m</td><td> $\theta_{\text{inc}}$  (°)</td><td> $d_{\text{Mo}}$  (nm)</td><td> $d_{\text{Si}}$  (nm)</td><td>Re r</td><td>Im r</td><td> $R = |r|^{2}$ </td></tr><tr><td>1</td><td>1</td><td>1.50</td><td>2.9983</td><td>3.9348</td><td>0.710212</td><td>0.461336</td><td>0.717232</td></tr><tr><td>1</td><td>2</td><td>3.00</td><td>3.0000</td><td>3.9404</td><td>0.709757</td><td>0.462358</td><td>0.717530</td></tr><tr><td>1</td><td>3</td><td>4.52</td><td>3.0029</td><td>3.9500</td><td>0.708982</td><td>0.464086</td><td>0.718032</td></tr><tr><td>1</td><td>4</td><td>6.06</td><td>3.0071</td><td>3.9636</td><td>0.707865</td><td>0.466549</td><td>0.718741</td></tr><tr><td>1</td><td>5</td><td>7.62</td><td>3.0125</td><td>3.9816</td><td>0.706379</td><td>0.469771</td><td>0.719656</td></tr><tr><td>1</td><td>6</td><td>9.22</td><td>3.0194</td><td>4.0045</td><td>0.704467</td><td>0.473833</td><td>0.720792</td></tr><tr><td>1</td><td>7</td><td>10.86</td><td>3.0278</td><td>4.0328</td><td>0.702079</td><td>0.478784</td><td>0.722149</td></tr><tr><td>1</td><td>8</td><td>12.55</td><td>3.0380</td><td>4.0671</td><td>0.699135</td><td>0.484712</td><td>0.723736</td></tr><tr><td>1</td><td>9</td><td>14.32</td><td>3.0503</td><td>4.1089</td><td>0.695495</td><td>0.491802</td><td>0.725582</td></tr><tr><td>1</td><td>10</td><td>16.16</td><td>3.0650</td><td>4.1590</td><td>0.691065</td><td>0.500102</td><td>0.727673</td></tr><tr><td>1</td><td>11</td><td>18.11</td><td>3.0826</td><td>4.2197</td><td>0.685606</td><td>0.509892</td><td>0.730045</td></tr><tr><td>1</td><td>12</td><td>20.18</td><td>3.1039</td><td>4.2933</td><td>0.678903</td><td>0.521333</td><td>0.732697</td></tr><tr><td>1</td><td>13</td><td>22.41</td><td>3.1300</td><td>4.3837</td><td>0.670585</td><td>0.534758</td><td>0.735651</td></tr><tr><td>1</td><td>14</td><td>24.85</td><td>3.1628</td><td>4.4967</td><td>0.660149</td><td>0.550571</td><td>0.738925</td></tr><tr><td>1</td><td>15</td><td>27.57</td><td>3.2056</td><td>4.6410</td><td>0.646893</td><td>0.569262</td><td>0.742530</td></tr><tr><td>1</td><td>16</td><td>30.67</td><td>3.2643</td><td>4.8311</td><td>0.629874</td><td>0.591367</td><td>0.746457</td></tr><tr><td>1</td><td>17</td><td>34.38</td><td>3.3532</td><td>5.0975</td><td>0.607430</td><td>0.617873</td><td>0.750738</td></tr><tr><td>1</td><td>18</td><td>39.19</td><td>3.5124</td><td>5.5133</td><td>0.576892</td><td>0.650115</td><td>0.755454</td></tr><tr><td>1</td><td>19</td><td>47.79</td><td>4.0065</td><td>6.5082</td><td>0.525839</td><td>0.696983</td><td>0.762293</td></tr><tr><td>2</td><td>1</td><td>0.37</td><td>2.9978</td><td>3.9331</td><td>0.710353</td><td>0.461016</td><td>0.717138</td></tr><tr><td>2</td><td>2</td><td>0.75</td><td>2.9979</td><td>3.9334</td><td>0.710325</td><td>0.461081</td><td>0.717157</td></tr><tr><td>2</td><td>3</td><td>1.11</td><td>2.9980</td><td>3.9340</td><td>0.710280</td><td>0.461182</td><td>0.717186</td></tr><tr><td>2</td><td>4</td><td>1.48</td><td>2.9983</td><td>3.9348</td><td>0.710216</td><td>0.461327</td><td>0.717229</td></tr><tr><td>2</td><td>5</td><td>1.83</td><td>2.9986</td><td>3.9357</td><td>0.710138</td><td>0.461503</td><td>0.717280</td></tr><tr><td>2</td><td>6</td><td>2.17</td><td>2.9989</td><td>3.9369</td><td>0.710046</td><td>0.461708</td><td>0.717340</td></tr><tr><td>2</td><td>7</td><td>2.50</td><td>2.9993</td><td>3.9381</td><td>0.709943</td><td>0.461941</td><td>0.717409</td></tr><tr><td>2</td><td>8</td><td>2.80</td><td>2.9997</td><td>3.9395</td><td>0.709836</td><td>0.462182</td><td>0.717479</td></tr><tr><td>2</td><td>9</td><td>3.09</td><td>3.0002</td><td>3.9409</td><td>0.709720</td><td>0.462440</td><td>0.717554</td></tr><tr><td>2</td><td>10</td><td>3.35</td><td>3.0006</td><td>3.9423</td><td>0.709607</td><td>0.462694</td><td>0.717628</td></tr><tr><td>2</td><td>11</td><td>3.57</td><td>3.0010</td><td>3.9436</td><td>0.709504</td><td>0.462924</td><td>0.717695</td></tr><tr><td>2</td><td>12</td><td>3.75</td><td>3.0013</td><td>3.9447</td><td>0.709415</td><td>0.463124</td><td>0.717753</td></tr><tr><td>2</td><td>13</td><td>3.88</td><td>3.0016</td><td>3.9455</td><td>0.709348</td><td>0.463273</td><td>0.717796</td></tr><tr><td>2</td><td>14</td><td>3.93</td><td>3.0017</td><td>3.9458</td><td>0.709321</td><td>0.463332</td><td>0.717814</td></tr><tr><td>2</td><td>15</td><td>3.90</td><td>3.0016</td><td>3.9456</td><td>0.709337</td><td>0.463297</td><td>0.717803</td></tr><tr><td>2</td><td>16</td><td>3.73</td><td>3.0013</td><td>3.9445</td><td>0.709425</td><td>0.463100</td><td>0.717746</td></tr><tr><td>2</td><td>17</td><td>3.38</td><td>3.0006</td><td>3.9425</td><td>0.709594</td><td>0.462724</td><td>0.717637</td></tr><tr><td>2</td><td>18</td><td>2.70</td><td>2.9996</td><td>3.9390</td><td>0.709873</td><td>0.462099</td><td>0.717454</td></tr><tr><td>2</td><td>19</td><td>1.01</td><td>2.9980</td><td>3.9338</td><td>0.710294</td><td>0.461150</td><td>0.717177</td></tr></table>

For the first mirror, the Mo layer thickness varies from 3.00 nm (small angles) to 4.01 nm $( m = 1 9 , \theta = 4 7 . 8 ^ { \circ } )$ while the Si layer thickness varies from 3.93 to 6.51 nm. The bilayer period $d = d _ { \mathrm { M o } } + d _ { \mathrm { S i } }$ grows from 6.93 nm at normal incidence to 10.51 nm at $\theta = 4 7 . 8 ^ { \circ }$ , following the trend of the approximate Bragg condition 2d cos $\theta \approx \lambda$ . Refraction is included through the layer-dependent expression used to initialize the optimization above. The reflectance R rises from 0.717 (m = 1) to 0.762 (m = 19) — as the angle of incidence increases, the efective penetration depth into the absorbing medium decreases, enhancing R. For the second mirror, all incidence angles remain small $( 0 . 3 7 ^ { \circ } - 3 . 9 3 ^ { \circ } )$ , so optimal thicknesses are virtually constant $( d _ { \mathrm { M o } } \approx 3 . 0 0$ nm, $d _ { \mathrm { S i } } \approx 3 . 9 4 ~ \mathrm { n m } )$ , and R varies only in the fourth decimal place (0.7171–0.7178). The small variation suggests that a common second-mirror coating can be a useful approximation. Its performance must be evaluated separately from the individually optimized designs tabulated here.

## 3.2.3 Configuration 2: λ = 11.2 nm, Ru/Be

The absorbing material is Ru $( \delta = 0 . 0 6 6 0 , \beta = 0 . 0 0 6 5 )$ and the spacer is Be $( \delta = - 0 . 0 1 2 2 , \beta = 0 . 0 0 1 3 )$ . A negative decrement indicates that the real part of the refractive index of Be at this wavelength exceeds unity, which occurs near the Be K-absorption edge at $\lambda \approx 1 1 . 3$ nm. Results are summarized in Table 6.

Table 6: Layer thicknesses of optimized Bragg mirrors for Example 4 (λ = 11.2 nm, Ru/Be, 60 layers, TE polarization). Notation as in Table 5.

<table><tr><td>Mirror</td><td>m</td><td> $\theta_{\text{inc}}$  (°)</td><td> $d_{\text{Ru}}$  (nm)</td><td> $d_{\text{Be}}$  (nm)</td><td>Re r</td><td>Im r</td><td> $R = |r|^{2}$ </td></tr><tr><td>1</td><td>1</td><td>1.50</td><td>2.3680</td><td>3.2983</td><td>0.669032</td><td>0.548699</td><td>0.748674</td></tr><tr><td>1</td><td>2</td><td>3.00</td><td>2.3690</td><td>3.3030</td><td>0.668303</td><td>0.549863</td><td>0.748979</td></tr><tr><td>1</td><td>3</td><td>4.52</td><td>2.3706</td><td>3.3112</td><td>0.667061</td><td>0.551835</td><td>0.749491</td></tr><tr><td>1</td><td>4</td><td>6.06</td><td>2.3730</td><td>3.3228</td><td>0.665274</td><td>0.554640</td><td>0.750215</td></tr><tr><td>1</td><td>5</td><td>7.62</td><td>2.3761</td><td>3.3382</td><td>0.662905</td><td>0.558308</td><td>0.751151</td></tr><tr><td>1</td><td>6</td><td>9.22</td><td>2.3801</td><td>3.3577</td><td>0.659869</td><td>0.562927</td><td>0.752314</td></tr><tr><td>1</td><td>7</td><td>10.86</td><td>2.3848</td><td>3.3817</td><td>0.656092</td><td>0.568551</td><td>0.753707</td></tr><tr><td>1</td><td>8</td><td>12.55</td><td>2.3906</td><td>3.4110</td><td>0.651459</td><td>0.575275</td><td>0.755340</td></tr><tr><td>1</td><td>9</td><td>14.32</td><td>2.3974</td><td>3.4466</td><td>0.645757</td><td>0.583304</td><td>0.757246</td></tr><tr><td>1</td><td>10</td><td>16.16</td><td>2.4055</td><td>3.4893</td><td>0.638855</td><td>0.592685</td><td>0.759412</td></tr><tr><td>1</td><td>11</td><td>18.11</td><td>2.4152</td><td>3.5411</td><td>0.630395</td><td>0.603726</td><td>0.761883</td></tr><tr><td>1</td><td>12</td><td>20.18</td><td>2.4266</td><td>3.6039</td><td>0.620054</td><td>0.616599</td><td>0.764661</td></tr><tr><td>1</td><td>13</td><td>22.41</td><td>2.4405</td><td>3.6810</td><td>0.607272</td><td>0.631665</td><td>0.767780</td></tr><tr><td>1</td><td>14</td><td>24.85</td><td>2.4578</td><td>3.7773</td><td>0.591268</td><td>0.649364</td><td>0.771271</td></tr><tr><td>1</td><td>15</td><td>27.57</td><td>2.4799</td><td>3.9005</td><td>0.570921</td><td>0.670234</td><td>0.775164</td></tr><tr><td>1</td><td>16</td><td>30.67</td><td>2.5099</td><td>4.0629</td><td>0.544631</td><td>0.694871</td><td>0.779469</td></tr><tr><td>1</td><td>17</td><td>34.38</td><td>2.5550</td><td>4.2910</td><td>0.509401</td><td>0.724400</td><td>0.784245</td></tr><tr><td>1</td><td>18</td><td>39.19</td><td>2.6367</td><td>4.6471</td><td>0.459810</td><td>0.760344</td><td>0.789548</td></tr><tr><td>1</td><td>19</td><td>47.79</td><td>2.9083</td><td>5.4854</td><td>0.373591</td><td>0.810425</td><td>0.796359</td></tr><tr><td>2</td><td>1</td><td>0.37</td><td>2.3677</td><td>3.2968</td><td>0.669260</td><td>0.548334</td><td>0.748579</td></tr><tr><td>2</td><td>2</td><td>0.75</td><td>2.3677</td><td>3.2971</td><td>0.669214</td><td>0.548407</td><td>0.748598</td></tr><tr><td>2</td><td>3</td><td>1.11</td><td>2.3678</td><td>3.2975</td><td>0.669142</td><td>0.548523</td><td>0.748628</td></tr><tr><td>2</td><td>4</td><td>1.48</td><td>2.3680</td><td>3.2982</td><td>0.669039</td><td>0.548688</td><td>0.748672</td></tr><tr><td>2</td><td>5</td><td>1.83</td><td>2.3681</td><td>3.2990</td><td>0.668914</td><td>0.548888</td><td>0.748724</td></tr><tr><td>2</td><td>6</td><td>2.17</td><td>2.3683</td><td>3.3000</td><td>0.668767</td><td>0.549123</td><td>0.748786</td></tr><tr><td>2</td><td>7</td><td>2.50</td><td>2.3686</td><td>3.3011</td><td>0.668601</td><td>0.549389</td><td>0.748855</td></tr><tr><td>2</td><td>8</td><td>2.80</td><td>2.3688</td><td>3.3022</td><td>0.668429</td><td>0.549663</td><td>0.748927</td></tr><tr><td>2</td><td>9</td><td>3.09</td><td>2.3691</td><td>3.3034</td><td>0.668244</td><td>0.549958</td><td>0.749003</td></tr><tr><td>2</td><td>10</td><td>3.35</td><td>2.3693</td><td>3.3046</td><td>0.668062</td><td>0.550247</td><td>0.749079</td></tr><tr><td>2</td><td>11</td><td>3.57</td><td>2.3695</td><td>3.3057</td><td>0.667897</td><td>0.550509</td><td>0.749147</td></tr><tr><td>2</td><td>12</td><td>3.75</td><td>2.3697</td><td>3.3066</td><td>0.667754</td><td>0.550736</td><td>0.749206</td></tr><tr><td>2</td><td>13</td><td>3.88</td><td>2.3699</td><td>3.3073</td><td>0.667646</td><td>0.550908</td><td>0.749251</td></tr><tr><td>2</td><td>14</td><td>3.93</td><td>2.3699</td><td>3.3076</td><td>0.667604</td><td>0.550975</td><td>0.749268</td></tr><tr><td>2</td><td>15</td><td>3.90</td><td>2.3699</td><td>3.3075</td><td>0.667630</td><td>0.550934</td><td>0.749258</td></tr><tr><td>2</td><td>16</td><td>3.73</td><td>2.3697</td><td>3.3065</td><td>0.667770</td><td>0.550711</td><td>0.749199</td></tr><tr><td>2</td><td>17</td><td>3.38</td><td>2.3693</td><td>3.3048</td><td>0.668040</td><td>0.550282</td><td>0.749088</td></tr><tr><td>2</td><td>18</td><td>2.70</td><td>2.3687</td><td>3.3018</td><td>0.668488</td><td>0.549568</td><td>0.748902</td></tr><tr><td>2</td><td>19</td><td>1.01</td><td>2.3678</td><td>3.2974</td><td>0.669165</td><td>0.548486</td><td>0.748619</td></tr></table>

The $\mathrm { R u / B e }$ material combination at $\lambda = 1 1 . 2$ nm provides markedly higher reflectance than $\mathrm { M o } / \mathrm { S i }$ at $\lambda = 1 3 . 5$ nm. R on the first mirror ranges from 0.749 (m = 1) to $0 . 7 9 6 \ ( m = 1 9 )$ , which is $3 { - } 4$ percentage points higher than for $\mathrm { M o / S i ~ ( 0 . 7 1 7 - 0 . 7 \tilde { 6 } 2 ) }$ . This is attributable to the lower absorption of Be $( \beta _ { \mathrm { B e } } = 0 . 0 0 1 \bar { 3 } )$ relative to Si $( \beta _ { \mathrm { S i } } = 0 . 0 \dot { 0 } 1 8 )$ and the larger refractive index contrast of $\mathrm { R u / B e }$ . As with $\mathrm { M o / S i }$ , for the second mirror (small angles $0 . 3 7 ^ { \circ } { - 3 . 9 3 ^ { \circ } } )$ optimal layer thicknesses are practically constant: $d _ { \mathrm { R u } } \approx 2 . 3 7$ nm, $d _ { \mathrm { B e } } \approx 3 . 3 0$ nm, $R \approx 0 . 7 4 9$

## 3.2.4 Discussion

Maximizing reflectance over layer thicknesses at a fixed target angle does not force the maximum of the angular reflectance curve to occur at that angle. For example, for $m = 1$ on the second mirror, the target is $0 . 3 7 ^ { \circ }$ whereas the local near-normal maxima of the tabulated $\mathrm { M o / S i }$ and Ru/Be designs occur at approximately $1 . 9 0 ^ { \circ }$ and $2 . 0 0 ^ { \circ }$ , respectively. The tabulated reflectances are evaluated at the actual target angles. The angular-peak ofset is not an optimization constraint.

Comparison with the typical reflectance $R \sim 7 0 \%$ of standard $\mathrm { M o } / \mathrm { S i }$ coatings (50 bilayers, $\lambda = 1 3 . 5$ nm, incident angle $\sim 6 ^ { \circ } )$ indicates that individually optimized 30-bilayer coatings achieve comparable or superior reflectance $\breve { (} R = 7 1 . 7 \% - 7 6 . 2 \% )$ with fewer layers in the ideal model. This comparison is not an experimental coating-performance validation, because the calculation omits interface roughness, interdifusion, and fabrication errors. For Ru/Be at $\lambda = 1 1 . 2$ nm, reflectance is even higher (74.9%–79.6%). The fraction of the power leaving the mask in an accepted order that is retained after the two modeled reflections is $R _ { 1 } R _ { 2 } \approx 5 1 . 5 \%$ $\mathrm { ( M o / S i } $ , low angles) to 59.6% (Ru/Be, m = 19), exceeding the throughput of 6- and 10-mirror systems (12% and 2.8%, respectively) by up to a factor of ∼ 20.

## 3.3 Mask Optimization for a Target Aerial Image on the Wafer

This section is dedicated to mask optimization for a prescribed field profile on the wafer in the synthesized projection system. Mask optimization is conducted using approaches developed in [26].

## 3.3.1 Formulation of the Inverse Problem

In Example 4, the optical path lengths of the channels with $1 \leq | n | \leq N = 1 9$ are equalized $( P _ { n } \approx 2 9 9 8 . 1 \ : \mathrm { m m } )$ removing order-dependent propagation phase shifts. The relative phases at the wafer still depend on the mask amplitudes and on the complex reflection coeficients of both Bragg coatings. Let $A _ { n }$ denote the complex electric-field amplitude of mask order $n ,$ and let $r _ { 1 , n }$ and $r _ { 2 , n }$ denote the corresponding facet reflection coeficients. With the common propagation phase omitted and amplitudes referenced to $\zeta _ { \mathrm { w } } = 0$ , the wafer coeficient is

$$
B _ {- n} = r _ {2, n} r _ {1, n} A _ {n}.\tag{19}
$$

Coeficients $r _ { 1 , n }$ and $r _ { 2 , n }$ were determined previously (Table 6) for $\lambda = 1 1 . 2$ nm, $\mathrm { R u / B e }$ . The field on the wafer is evaluated via $\operatorname { E q . } \ ( 3 )$ . Let $\mathbf { E } ^ { ( d ) }$ and $I ^ { ( d ) } = | \mathbf { E } ^ { ( d ) } | ^ { 2 }$ denote the target electric field distribution and intensity on the wafer. The objective of Inverse Lithography Technology (ILT) is to determine the spatial permittivity distribution $\varepsilon _ { j } ( x )$ of the mask layers such that the projected aerial intensity matches the target

intensity:

$$
\left| \mathbf {E} ^ {\mathrm{(w)}} \right| ^ {2} = \left| \mathbf {E} ^ {(d)} \right| ^ {2}.\tag{20}
$$

We consider a mask comprising a single absorber layer with permittivity $\varepsilon ( x )$ positioned atop multilayer mirror layers that are homogeneous along x.

## 3.3.2 Forward Problem

Scattering amplitudes $A _ { n }$ for a given profile $\varepsilon ( x )$ are evaluated using the modal waveguide method (equivalent to RCWA). The mask consists of an absorber layer of thickness $d _ { \mathrm { a b s } }$ with periodically modulated permittivity $\begin{array} { r } { \varepsilon ( x ) = \sum _ { m } \varepsilon _ { m } \exp ( - \mathrm { i } \kappa _ { x } m x ) } \end{array}$ (where $\varepsilon _ { m }$ are Fourier coeficients), situated on a Bragg mirror $\mathrm { ( R \bar { u } / B e / S r }$ , 30 periods $[ 2 0 ] )$ . The solution proceeds as follows.

The electric field inside the absorber layer is represented as $E _ { y } ( x , z ) = X ( x ) Z ( z )$ . The transverse function $X ( x )$ is expanded in a Fourier series over plane waves $\psi _ { m } = \exp ( - \mathrm { i } \kappa _ { x } m x )$ , and the longitudinal function is $Z ( z ) = \exp ( \pm \mathrm { i } k _ { z } z )$

Substituting into the Helmholtz equation yields the algebraic eigenvalue problem:

$$
\hat {D} \mathbf {B} _ {p} = k _ {z; p} ^ {2} \mathbf {B} _ {p}, \qquad \hat {D} _ {n m} = k _ {0} ^ {2} \varepsilon_ {n - m} - (\kappa_ {x} n) ^ {2} \delta_ {n m},\tag{21}
$$

where $k _ { z ; p } ^ { 2 }$ are the eigenvalues and $k _ { z ; p }$ are the longitudinal wavenumbers of the modes, and $\mathbf { B } _ { p }$ are the eigenvectors (components $B _ { p , m }$ define the contribution of the m-th plane wave to the p-th mode). Matrix $\hat { D }$ has dimensions $( 2 M + 1 ) \times \mathsf { \bar { ( 2 M + 1 ) } }$ .

The field in each layer is expressed via modal expansions:

$$
E _ {y} ^ {(j)} (x, z) = k _ {0} \sum_ {p = - M} ^ {M} \left[ A _ {p; 1} ^ {(j)} \mathrm{e} ^ {\mathrm{i} k _ {z; p} ^ {(j)} z} + A _ {p; 2} ^ {(j)} \mathrm{e} ^ {- \mathrm{i} k _ {z; p} ^ {(j)} z} \right] \sum_ {m = - M} ^ {M} B _ {p, m} ^ {(j)} \psi_ {m}.\tag{22}
$$

Coeficients $A _ { p ; 1 } ^ { ( j ) } , A _ { p ; 2 } ^ { ( j ) }$ are determined from tangential field continuity $( E _ { y }$ and $H _ { x } )$ across layer boundaries, yielding the linear system:

$$
\hat {\mathbf {M}} \mathbf {X} = \mathbf {R},\tag{23}
$$

where X is the vector of unknown modal coeficients (reflected waves and waves transmitted into and through the mirror), and R describes the incident wave. Solving Eq. (23) yields modal coeficients that must be converted to electric-field amplitudes. In the implemented normalization, $A _ { n } = - k _ { 0 } X _ { n } ^ { ( r ) } \ ( n = - M , \ldots , M )$ where $X _ { n } ^ { ( r ) }$ is the reflected-wave block of X. The minus sign follows its polarization convention. Here and in $\operatorname { E q . } { \big ( } 1 9 { \big ) } , A _ { n }$ denotes the converted electric-field amplitude, not the raw modal coeficient. The reflected field above the mask $( z > 0 )$ is:

$$
E _ {y} ^ {(r)} (x, z) = \sum_ {n = - M} ^ {M} A _ {n} \exp (- \mathrm{i} \kappa_ {x} n x - \mathrm{i} k _ {z; n} z).\tag{24}
$$

## 3.4 Optimization via Fourier-Parameterized Projection

To solve the inverse problem of finding $\varepsilon ( x )$ from the target wafer aerial image, we apply gradient-based optimization with Fourier-parameterized mask projection [26].

Instead of optimizing hundreds of discrete pixels, a smooth latent function is introduced:

$$
f _ {\mathrm{latent}} (x) = \mathrm{Re} \left(\sum_ {m = - M} ^ {M} F _ {m} \mathrm{e} ^ {- \mathrm{i} \kappa_ {x} m x}\right),\tag{25}
$$

where $F _ { m }$ are the complex Fourier coeficients to be optimized. The physical absorber density is obtained via a steepened sigmoid mapping:

$$
\rho (x) = \sigma \big (\beta f _ {\text { latent }} (x) \big) \in (0, 1),\tag{26}
$$

where $\beta$ is a steepness parameter increased during optimization to enforce binarization. The permittivity is computed as:

$$
\varepsilon (x) = \varepsilon_ {\mathrm{vac}} + \rho (x) (\varepsilon_ {\mathrm{abs}} - \varepsilon_ {\mathrm{vac}}),\tag{27}
$$

where $\varepsilon _ { \mathrm { v a c } } = 1$ and $\varepsilon _ { \mathrm { a b s } }$ is the absorber permittivity. The nonlinearity of σ allows a finite set of $F _ { m }$ to generate an infinite high-frequency spectrum for $\varepsilon ( x )$ , suppressing the Gibbs phenomenon.

The inverse problem is to minimize the loss functional measuring the discrepancy between the intensities of the reflected and target fields on the wafer:

$$
\varepsilon (x) = \arg \min _ {\varepsilon} \mathcal {L} (\varepsilon),\tag{28}
$$

where the total loss is:

$$
\mathcal {L} = \mathcal {L} _ {\mathrm{shape}} + \mathcal {L} _ {\mathrm{bin}} + \mathcal {L} _ {\mathrm{HF}} + \mathcal {L} _ {\mathrm{supp}}.\tag{29}
$$

Here:

$\mathcal { L } _ { \mathrm { s h a p e } } = \mathrm { M S E } ( I _ { \mathrm { w } } ^ { \mathrm { n o r m } } , I _ { \mathrm { t a r g e t } } ^ { \mathrm { n o r m } } )$ is the mean squared error between normalized wafer intensity and target profile, where $I _ { \mathrm { w } } ( x ) = | E _ { y } ^ { ( \mathrm { w } ) } ( x ) | ^ { 2 }$ with $B _ { - n } = r _ { 2 , n } r _ { 1 , n } A _ { n }$

$\mathcal { L } _ { \mathrm { b i n } } = \langle \rho ( 1 - \rho ) \rangle$ ⟩ penalizes intermediate grayscale density values, promoting binary solutions $( \rho \to 0$ or 1).

$\begin{array} { r } { \mathcal { L } _ { \mathrm { H F } } = w _ { \mathrm { H F } } \sum _ { m = 1 } ^ { N _ { \mathrm { F R } } } m \vert F _ { m } \vert ^ { 2 } } \end{array}$ penalizes unphysical high-frequency spatial components, discouraging fine-scale structure without imposing a minimum manufacturable feature size (where $N _ { \mathrm { F R } } = M$ is the Fourier truncation order).

$\mathcal { L } _ { \mathrm { s u p p } } = w _ { \mathrm { s u p p } } ( \alpha ) | A _ { - \tilde { m } } | ^ { 2 }$ suppresses scattering into the unused back-reflection order −m˜ that coincides with the input illumination aperture (this term is not present in [26]).

In our experiments, the target intensity $I ^ { ( d ) }$ is binary, with unity in target regions and zero elsewhere. In the global wafer coordinates we prescribe $E _ { y } ^ { ( d ) } ( x ) = \sqrt { I ^ { ( d ) } ( x ) } \exp ( + 4 \mathrm { i } k _ { 0 x } x )$ , where $k _ { 0 x } = k _ { 0 } \sin 6 ^ { \circ } = \tilde { m } \kappa _ { x }$ . The numerical plots use the reversed wafer coordinate $x _ { \mathrm { p } } = - x$ (and $y _ { \mathrm { p } } = - y$ in 3D), so the implemented phase is $\exp ( - 4 \mathrm { i } \bar { k } _ { 0 x } x _ { \mathrm { p } } )$ . This convention accounts for the inversion of the transverse wavevector by the projection geometry. Decomposing the target field into spatial harmonics and retaining the selected wafer orders yields the bandlimited target intensity $\tilde { I } ^ { ( d ) }$ used in Eq. (29). The imposed phase is a modeling choice that afects this filtered target.

The optimization procedure runs as follows: for the first 40% of epochs, only the image shape is optimized $( \mathcal { L } _ { \mathrm { b i n } } \bar { = } 0 , \beta = 1 )$ . Subsequently, $\beta$ is annealed up to $\sim 1 5$ while the weight of ${ \mathcal { L } } _ { \mathrm { b i n } }$ increases to $5 ,$ driving the mask toward a strict binary profile without violating physical admissibility. Optimization starts from an unconstrained latent field and converges to a physical density $\rho ( x )$ that, after hard thresholding at 0.5, defines the synthesized mask layout.

We use the Adam optimizer with a learning rate of $5 \times 1 0 ^ { - 3 }$ for 500 epochs. Gradients are computed via automatic diferentiation through the full physical solver: $\partial \mathcal { L } / \partial \Theta = ( \partial \mathcal { L } / \partial \mathbf { E } ^ { ( r ) } ) ( \partial \mathbf { E } ^ { ( r ) } / \partial \boldsymbol { \varepsilon } ) ( \partial \boldsymbol { \varepsilon } / \partial \bar { \Theta } )$ , where $\Theta = \{ F _ { m } \}$

Optimization was conducted for $\lambda = 1 1 . 2$ nm. Mask and projection parameters:

• Wavelength $\lambda = 1 1 . 2$ nm, incidence angle $6 ^ { \circ }$ , TE polarization.

• Mask period $L _ { x } \approx 8 5 7$ nm, wafer period $L _ { x } ^ { \mathrm { ( w ) } } = L _ { x } / 4 \approx 2 1 4$ nm.

• Maximum harmonic index on the mask $M = 2 5$ , on the wafer $N = 1 9$

• Mask absorber: La $( \delta = - 0 . 0 4 4 0 , \beta = 0 . 0 1 5 9 )$ with thickness $d _ { \mathrm { a b s } } = 6 0 ~ \mathrm { n m }$ .

• Bragg mirror beneath the absorber: 30 periods of $\mathrm { R u / B e / S r ~ } \left( d _ { \mathrm { R u } } \ : = \ : 1 . 7 \right.$ nm, $d _ { \mathrm { B e } } ~ = ~ 2 . 7$ nm, $d _ { \mathrm { S r } } = 1 . 3 4 ~ \mathrm { n m } )$ ).

• Mirror reflection coeficients $r _ { 1 , n } , r _ { 2 , n }$ taken from Table $6 \left( \mathrm { R u / B e } , 3 0 \mathrm { b i l a y e r s } \right)$

• Target profile on the wafer: intensity maximum at $x = 0$ within the cell $[ - 1 0 7 , 1 0 7 ] \ \mathrm { n m }$

• Fourier expansion parameter $M _ { \mathrm { o p t } } = M = 2 5$ (the truncation order of the latent-function expansion, $N _ { \mathrm { F R } }$ in Eq. (29)), 500 epochs.

## 3.4.1 Results of Optimizations

The unfiltered target intensity is non-zero over $x \in [ - 2 . 3 , 2 . 3 ]$ nm, corresponding to a rectangular width of 4.6 nm. The full width at half maximum (FWHM) estimated from the plotted bandlimited target is approximately 5.1 nm, whereas that of the synthesized central peak is approximately 5.4 nm. These widths difer from the unfiltered target width and are not fixed a priori to $\lambda / 2$

Figure 11a illustrates the optimized continuous absorber density $\rho ( x )$ . In Fig. 11b, the binarized mask layout $( \tilde { \rho ( x ) } \in \{ 0 , 1 \} )$ is shown. The mask period $L _ { x }$ ≈ 857 nm contains several absorber features synthesized to shape the required difraction spectrum, whose fabrication by electron-beam lithography would require separate verification of minimum widths, gaps, and fabrication tolerances.

![](images/e7e757eefb671d5d32716b0f17db0e7fbf8161b1c0a9e90c328b115bc27e187b.jpg)

![](images/90f0da4a6c606c8722b5f9d20e379ca52a03e905c66d9819fc063e02c3b3bbc9.jpg)  
Figure 11: (a) Absorber density distribution $\rho ( x )$ in the optimized mask $( \lambda = 1 1 . 2$ nm, La absorber, 500 epochs). (b) Binarized mask profile $( \rho \in \{ 0 , 1 \}$ at threshold $\rho > 0 . 5 )$

Figure 12 compares the target aerial image with the optimized result across $[ - L _ { x } / 2 , L _ { x } / 2 ] = [ - 4 2 8 . 6 , 4 2 8 . 6 ]$ nm. The field repeats with period $L _ { x } ^ { \mathrm { ( w ) } } = 2 1 4$ nm. The peak profile is reproduced with low error $( { \mathcal { L } } _ { \mathrm { s h a p e } } =$ $1 . 6 \times 1 0 ^ { - 5 } )$ . The peak intensity ratio reaches max $I / I _ { \mathrm { i n c } } = 0 . 9 4 7$ (94.7% of incident intensity), which exceeds the baseline two-reflection reflectance $R ^ { 2 } \approx ( 0 . 7 4 9 ) ^ { 2 } \approx 5 6 \%$ due to constructive interference among the difracted orders.

Figure 13 depicts the harmonic amplitude spectra $\vert A _ { m } \vert$ (scattered by the mask) and $| B _ { - m } | = | r _ { 2 , m } r _ { 1 , m } A _ { m } |$ (incident on the wafer). The specular reflection order $m = 8$ (coinciding with the incident-beam order $\tilde { m } = 8 )$ dominates, while higher orders decay with |m|. The coeficients $B _ { - m }$ are additionally modulated by $r _ { 1 , m }$ and $r _ { 2 , m }$ and largely follow the behavior of $\vert A _ { m } \vert$ . The plotted wafer spectrum is indexed by its originating mask order $m ,$ , so its coeficient is $B _ { - m }$ in the global-coordinate convention.

We next evaluated mask synthesis for an aerial image with two closely spaced intensity peaks in Example 4, targeting two 6-nm-wide lines separated by a 6-nm space within the periodic cell. Figure $^ { \mathrm { 1 4 ( a , b ) } }$ shows the simulated image and the synthesized binary mask. These are aerial-image calculations, not a resist-printing simulation.

To evaluate sensitivity to axial wafer displacement, the field was computed for wafer displacements $\Delta z \in$ [0, 5] nm. As shown in Fig. $1 4 ( \mathrm { c } )$ , the two peaks remain resolved for the tested defocus values. The calculation does not establish a complete focus–dose process window.

![](images/0fe415497e7d3aa3864693099f3c1847738948b53784b5756bee41d46038280a.jpg)

![](images/5bbd5fe18df21130cbe117873efd84bd5ac2acf82af81a11ebf5606ca1c9eccd.jpg)  
Figure 12: Aerial intensity on the wafer across $[ - L _ { x } / 2 , L _ { x } / 2 ]$ : target profile (dashed line), bandlimited target with propagating orders (dash-dotted line), and optimized result (solid line). The peak intensity ratio is max $I / I _ { \mathrm { i n c } } = 0 . 9 4 7$ . Periodicity $L _ { x } ^ { \mathrm { ( w ) } } = 2 1 4 ~ \mathrm { n m }$

![](images/17140fb046e341a5592afde5a5080ce3d0717171d0620da6a86936990ded4b02.jpg)

![](images/d0d91112a90b4e5a812464ec25adc6a8c4ef8e5754210c1df2121ab6355ee482.jpg)  
Figure 13: Field amplitude spectra: (a) is $\vert A _ { m } \vert$ scattered by the mask, (b) is the wafer spectrum indexed by the originating mask order, corresponding to $| \dot { B } _ { - m } |$ in global coordinates.

## 4 3D Two-Mirror Projection System

## 4.1 Problem Formulation and Basic Equations

The preceding analysis addressed a 2D formulation (TE polarization, $\mathbf { E } \parallel \mathbf { y } ;$ , mask invariant along y). In three dimensions, the mask represents a 2D periodic structure with spatial periods $L _ { x }$ along x and $L _ { u }$ along y (assuming $L _ { x } = L _ { y } ,$ a square lattice). The mask occupies the domain $[ - \hat { L / 2 } , L / 2 ] \stackrel { - } { \times } [ - L / 2 , L / 2 ] \times [ - D , 0 ]$ in Cartesian coordinates $( x , y , z )$ . A TE-polarized beam is incident at $6 ^ { \circ }$ to the z-axis in the xz-plane: $\mathbf { k } _ { 0 } = ( k _ { 0 } \sin ( \pi / 3 0 ) , 0 , - k _ { 0 } \cos ( \pi / 3 0 ) )$ (the beam propagates toward the mask, in the −z direction).

![](images/116ca705e6698a6042f6ad0cb3687b3681a0b49404b7cc2ce223b0468088b6c6.jpg)  
x (nm)

![](images/6d9acb246edd54b08952ffa1a71e50dbf73edcc49081666a95dd132514cf504e.jpg)

![](images/d2a28e861e0502b709ec2533aea78ca922e763ba6e63e08c0e70775506cee088.jpg)  
Figure 14: (a) Normalized aerial intensity on the wafer across $[ - L _ { x } / 8 , L _ { x } / 8 ]$ : target profile (dashed), bandlimited target (dash-dotted), and optimized result (solid). The peak intensity ratio is max $I / I _ { \mathrm { i n c } } = 0 . 8 1 \dot { 8 }$ Periodicity $L _ { x } ^ { \mathrm { ( w ) } } = 2 1 4$ nm. (b) Synthesized binary mask profile $( \rho \in \{ 0 , 1 \} )$ . (c) Normalized wafer aerial intensity under wafer defocus along the z-axis for $\Delta z = 0 , \ldots , 5$ nm.

The transverse component of the scattered electric field outside the mask is expanded in a double Fourier series:

$$
\left[ \begin{array}{c} E _ {x} ^ {(r)} \\ E _ {y} ^ {(r)} \end{array} \right] = \sum_ {m = - \infty} ^ {\infty} \sum_ {n = - \infty} ^ {\infty} \left[ \begin{array}{c} A _ {x; m, n} ^ {(r)} \\ A _ {y; m, n} ^ {(r)} \end{array} \right] \exp \bigl (- \mathrm{i} \kappa_ {x} m x - \mathrm{i} \kappa_ {y} n y - \mathrm{i} k _ {z; m, n} z \bigr),\tag{30}
$$

where $A _ { x ; m , n } ^ { ( r ) }$ and $A _ { y ; m , n } ^ { ( r ) }$ are the amplitudes of the $( m , n )$ -th harmonic, the superscript (r) denotes the reflected (mask-side) field, $\kappa _ { x } = 2 \pi / L _ { x } , \kappa _ { y } = 2 \pi / L _ { y } ,$ , and $k _ { z ; m , n } = \left( k _ { 0 } ^ { 2 } - \kappa _ { x } ^ { 2 } m ^ { 2 } - \kappa _ { y } ^ { 2 } n ^ { 2 } \right) ^ { 1 / 2 } \left( \mathrm { I m } k _ { z ; m , n } \leq 0 \right)$ Propagating orders satisfy $\kappa _ { x } ^ { 2 } m ^ { 2 } + \kappa _ { y } ^ { 2 } n ^ { 2 } \leq k _ { 0 } ^ { 2 } ~ ( M = \lfloor k _ { 0 } / \kappa _ { x } \rfloor$ , the maximum order along each axis). The propagating field in the GO beam approximation is:

$$
\left[ \begin{array}{c}E_{x}^{(r)}\\ E_{y}^{(r)} \end{array} \right] = \sum_{\substack{m,n\\ \kappa_{x}^{2}m^{2} + \kappa_{y}^{2}n^{2}\leq k_{0}^{2}}}\left[ \begin{array}{c}\tilde{A}_{x;m,n}^{(r)}(x,y,z)\\ \tilde{A}_{y;m,n}^{(r)}(x,y,z) \end{array} \right]\exp \bigl (-\mathrm{i}\kappa_{x}mx - \mathrm{i}\kappa_{y}ny - \mathrm{i}k_{z;m,n}z\bigr),\tag{31}
$$

where $\tilde { A } _ { x ; m , n } ^ { ( r ) }$ and $\tilde { A } _ { y ; m , n } ^ { ( r ) }$ are the amplitudes within the beam of order $( m , n )$ , and zero elsewhere.

The field on the wafer under 4× demagnification $( L _ { x } ^ { \mathrm { ( w ) } } = L _ { x } / 4 , L _ { y } ^ { \mathrm { ( w ) } } = L _ { y } / 4 )$ is:

$$
\left[ \begin{array}{c} E _ {x} ^ {\mathrm{(w)}} \\ E _ {y} ^ {\mathrm{(w)}} \end{array} \right] = \sum_ {(m, n) \in \mathcal {D} _ {N}} \left[ \begin{array}{c} B _ {x; m, n} ^ {\mathrm{(w)}} \\ B _ {y; m, n} ^ {\mathrm{(w)}} \end{array} \right] \exp \bigl (- \mathrm{i} \kappa_ {x} ^ {\mathrm{(w)}} m x - \mathrm{i} \kappa_ {y} ^ {\mathrm{(w)}} n y - \mathrm{i} k _ {z; m, n} ^ {\mathrm{(w)}} \zeta_ {\mathrm{w}} \bigr),\tag{32}
$$

where $k _ { z ; m , n } ^ { ( \mathbf { w } ) } = \bigl [ k _ { 0 } ^ { 2 } - ( \kappa _ { x } ^ { ( \mathbf { w } ) } m ) ^ { 2 } - ( \kappa _ { y } ^ { ( \mathbf { w } ) } n ) ^ { 2 } \bigr ] ^ { 1 / 2 } , \kappa _ { x } ^ { ( \mathbf { w } ) } = 4 \kappa _ { x } , \kappa _ { y } ^ { ( \mathbf { w } ) } = 4 \kappa _ { y } ,$ and $\left( \mathrm { w } \right)$ denotes the wafer-side field. Here $\zeta _ { \mathrm { w } } = z - Z _ { 1 }$ , and the coeficients are referenced to the wafer plane. For the square lattice, harmonics propagating toward the wafer satisfy $m ^ { 2 } + n ^ { 2 } < [ k _ { 0 } / ( 4 \kappa _ { x } ) ] ^ { 2 }$ We select the smaller circular aperture $m ^ { \mathrm { 2 } } + n ^ { \mathrm { 2 } } \leq \tilde { N } ^ { 2 }$ , where $N = \lfloor k _ { 0 } / ( 4 \kappa _ { x } ) \rfloor = 1 9$ This aperture is a design choice, not the exact propagation boundary. At the stated parameters, 24 additional propagating orders lie outside it. The selected domain is

$$
\mathcal {D} _ {N} = \{(m, n) \in \mathbb {Z} ^ {2}: m ^ {2} + n ^ {2} \leq N ^ {2}, (m, n) \neq (0, 0) \}.\tag{33}
$$

Each $( m , n ) \ – \mathrm { t h }$ beam is characterized by polar angle $\theta _ { m , n }$ (from the z-axis) and azimuthal angle $\varphi _ { m , n }$ (in the xy-plane):

$$
\sin \theta_ {m, n} = \frac {\left[ (\kappa_ {x} m) ^ {2} + (\kappa_ {y} n) ^ {2} \right] ^ {1 / 2}}{k _ {0}}, \qquad \varphi_ {m, n} = \mathrm{Arg} (m + \mathrm{i} n).\tag{34}
$$

On the wafer, the transverse wavevector, and hence sin $\theta ,$ is scaled by a factor of 4: sin $\theta _ { m , n } ^ { \mathrm { ( w ) } } = 4 \sin \theta _ { m , n }$ with $\mathrm { N A } _ { \mathrm { m a x } } = \sin \theta _ { N , 0 } ^ { \mathrm { ( w ) } } = 0 . 9 9 3$

The two-mirror system generalizes naturally to 3D. The first mirror is positioned in the plane $z = Z _ { 1 } =$ 1000 mm, with the center of facet (m, n) located at:

$$
(x _ {1} ^ {(m, n)}, y _ {1} ^ {(m, n)}, Z _ {1}) = \big (Z _ {1} \tan \theta_ {m, n} \cos \varphi_ {m, n}, Z _ {1} \tan \theta_ {m, n} \sin \varphi_ {m, n}, Z _ {1} \big).\tag{35}
$$

The second mirror redirects the beam toward the wafer center $( 0 , 0 , Z _ { 1 } )$ at angle $\theta _ { m , n } ^ { \mathrm { ( w ) } }$ . The facet center on the second mirror is positioned at:

$$
(x _ {f} ^ {(m, n)}, y _ {f} ^ {(m, n)}, z _ {f} ^ {(m, n)}) = \big (u _ {m, n} \tan \theta_ {m, n} ^ {\mathrm{(w)}} \cos \varphi_ {m, n}, u _ {m, n} \tan \theta_ {m, n} ^ {\mathrm{(w)}} \sin \varphi_ {m, n}, Z _ {1} - u _ {m, n} \big),\tag{36}
$$

where $u _ { m , n } = Z _ { 1 } - z _ { f } ^ { ( m , n ) }$ enforces equalized path lengths. The deflection angle $\beta _ { m , n }$ from the vertical satisfies:

$$
\tan \beta_ {m, n} = \frac {\left[ (x _ {f} - x _ {1}) ^ {2} + (y _ {f} - y _ {1}) ^ {2} \right] ^ {1 / 2}}{u _ {m , n}}.\tag{37}
$$

The total optical path length is:

$$
P _ {m, n} = \frac {Z _ {1}}{\cos \theta_ {m , n}} + \left[ (x _ {f} - x _ {1}) ^ {2} + (y _ {f} - y _ {1}) ^ {2} + u _ {m, n} ^ {2} \right] ^ {1 / 2} + \frac {u _ {m , n}}{\cos \theta_ {m , n} ^ {\mathrm{(w)}}}.\tag{38}
$$

Parameter $u _ { m , n }$ is determined by bisection to enforce $P _ { m , n } \approx 2 9 9 8 . 1$ mm. Incidence angles on the facets are $i _ { 1 } = ( \theta _ { m , n } + \beta _ { m , n } ) / 2$ , while $i _ { 2 }$ is computed via scalar products.

For a square grating $( L _ { x } = L _ { y } )$ , all radial parameters $( \theta , \theta ^ { ( \mathrm { w } ) } , z _ { f } , \rho _ { f } , \beta , i _ { 1 } , i _ { 2 } , P )$ , where $\rho _ { f } = ( x _ { f } ^ { 2 } + y _ { f } ^ { 2 } ) ^ { 1 / 2 }$ depend solely on the radius $r = \left( m ^ { 2 } + n ^ { 2 } \right) ^ { 1 / 2 }$ and are independent of $\varphi .$ . The facet coordinates $( x , y )$ are obtained via rotation by $\varphi \colon$

$$
x _ {1} = Z _ {1} \tan \theta \cos \varphi , y _ {1} = Z _ {1} \tan \theta \sin \varphi , x _ {f} = \rho_ {f} (r) \cos \varphi , y _ {f} = \rho_ {f} (r) \sin \varphi .\tag{39}
$$

Thus, the radial design reduces to the 2D problem (Example 4) by substituting $m  r$ . For non-integer r (most orders with $n \neq 0 )$ , the radial solution is obtained numerically by bisection, and the reflectances $\bar { R _ { 1 } } , R _ { 2 }$ are interpolated linearly over r from Table 6.

## 4.2 Design of the 3D Two-Mirror Projection System

## 4.2.1 Computational Parameters

Parameters match Example 4: $\lambda = 1 1 . 2$ nm, $L = 1 0$ mm, $L _ { x } = L _ { y } \approx 8 5 7$ nm, $Z _ { 1 } = 1 0 0 0 \ \mathrm { m m }$ , 4× demagnification, $M = 7 6 , N = 1 9 , \mathrm { { N A } _ { \mathrm { { m a x } } } = 0 . 9 9 3 }$ , and total optical path length 2998.1 mm. Harmonic $( m , n ) = ( - 8 , 0 )$ (the back-reflection) does not contribute to the aerial image because it coincides with the illumination input aperture.

The number of orders in the selected wafer aperture is 1128 (all integer pairs $( m , n )$ within $m ^ { 2 } + n ^ { 2 } \leq 1 9 ^ { 2 }$ excluding the origin). Each order maps to one facet on mirror 1 and one on mirror 2, yielding 2256 facets total. The number of unique r values is 132. Due to rotational symmetry, each r corresponds to 4 to 24 individual orders that share identical Bragg multilayer parameters.

## 4.2.2 Results for Facet Layouts

Table 7 lists facet centers, incidence angles, and interpolated reflectances for 21 representative orders $( m , n )$ The total optical path is $P _ { m , n } = 2 9 9 8 . 1$ mm across all orders. Facet tilt $\alpha _ { 1 }$ depends only on r and ranges from $0 . 7 5 ^ { \circ } \ \bar { ( } r = 1 )$ to $3 3 . 4 ^ { \circ } \ ( r = 1 9 )$ . For the second mirror, $\alpha _ { 2 }$ ranges from $2 . 6 \bar { ^ { \circ } }$ to $8 2 . 2 ^ { \circ }$

Table 7: Facet configurations of the first and second mirrors for the 3D case (λ = 11.2 nm, $L _ { x } = L _ { y } = 8 5 7$ nm, N = 19, NA = 0.993, $P = 2 9 9 8 . 1$ mm). $r = \left( m ^ { 2 } + n ^ { 2 } \right) ^ { 1 / 2 } , \varphi$ is azimuthal angle, $( x _ { 1 } , y _ { 1 } )$ is facet center on mirror 1 at $z = Z _ { 1 } = 1 0 0 0$ mm, $( x _ { f } , y _ { f } , z _ { f } )$ is facet center on mirror $2 , i _ { 1 }$ and $i _ { 2 }$ are incidence angles, $| R _ { 1 } R _ { 2 } |$ is product of reflectances (interpolated from Table 6).

<table><tr><td>m</td><td>n</td><td>r</td><td> $\varphi$  (°)</td><td> $x_1$  (mm)</td><td> $y_1$  (mm)</td><td> $x_f$  (mm)</td><td> $y_f$  (mm)</td><td> $z_f$  (mm)</td><td> $i_1$  (°)</td><td> $i_2$  (°)</td><td> $|R_1R_2|$ </td></tr><tr><td>1</td><td>0</td><td>1.000</td><td>0.0</td><td>13.1</td><td>0.0</td><td>52.2</td><td>0.0</td><td>2.0</td><td>1.50</td><td>0.37</td><td>0.560</td></tr><tr><td>1</td><td>1</td><td>1.414</td><td>45.0</td><td>13.1</td><td>13.1</td><td>52.2</td><td>52.2</td><td>3.2</td><td>2.12</td><td>0.53</td><td>0.561</td></tr><tr><td>2</td><td>1</td><td>2.236</td><td>26.6</td><td>26.1</td><td>13.1</td><td>104.6</td><td>52.3</td><td>6.5</td><td>3.36</td><td>0.83</td><td>0.561</td></tr><tr><td>2</td><td>2</td><td>2.828</td><td>45.0</td><td>26.1</td><td>26.1</td><td>104.6</td><td>104.6</td><td>9.9</td><td>4.26</td><td>1.05</td><td>0.561</td></tr><tr><td>3</td><td>0</td><td>3.000</td><td>0.0</td><td>39.2</td><td>0.0</td><td>157.0</td><td>0.0</td><td>11.0</td><td>4.52</td><td>1.11</td><td>0.561</td></tr><tr><td>3</td><td>2</td><td>3.606</td><td>33.7</td><td>39.2</td><td>26.2</td><td>157.2</td><td>104.8</td><td>15.6</td><td>5.45</td><td>1.33</td><td>0.561</td></tr><tr><td>4</td><td>3</td><td>5.000</td><td>36.9</td><td>52.4</td><td>39.3</td><td>210.2</td><td>157.7</td><td>29.4</td><td>7.62</td><td>1.83</td><td>0.562</td></tr><tr><td>5</td><td>0</td><td>5.000</td><td>0.0</td><td>65.5</td><td>0.0</td><td>262.8</td><td>0.0</td><td>29.4</td><td>7.62</td><td>1.83</td><td>0.562</td></tr><tr><td>7</td><td>0</td><td>7.000</td><td>0.0</td><td>91.8</td><td>0.0</td><td>370.2</td><td>0.0</td><td>58.3</td><td>10.86</td><td>2.50</td><td>0.564</td></tr><tr><td>5</td><td>5</td><td>7.071</td><td>45.0</td><td>65.6</td><td>65.6</td><td>264.5</td><td>264.5</td><td>59.5</td><td>10.98</td><td>2.52</td><td>0.565</td></tr><tr><td>8</td><td>5</td><td>9.434</td><td>32.0</td><td>105.3</td><td>65.8</td><td>427.7</td><td>267.3</td><td>110.2</td><td>15.11</td><td>3.21</td><td>0.568</td></tr><tr><td>7</td><td>7</td><td>9.899</td><td>45.0</td><td>92.2</td><td>92.2</td><td>375.1</td><td>375.1</td><td>122.6</td><td>15.97</td><td>3.32</td><td>0.569</td></tr><tr><td>10</td><td>0</td><td>10.000</td><td>0.0</td><td>131.8</td><td>0.0</td><td>536.2</td><td>0.0</td><td>125.4</td><td>16.16</td><td>3.35</td><td>0.569</td></tr><tr><td>10</td><td>7</td><td>12.207</td><td>35.0</td><td>132.4</td><td>92.6</td><td>543.5</td><td>380.5</td><td>199.1</td><td>20.63</td><td>3.78</td><td>0.573</td></tr><tr><td>13</td><td>0</td><td>13.000</td><td>0.0</td><td>172.4</td><td>0.0</td><td>710.7</td><td>0.0</td><td>232.5</td><td>22.41</td><td>3.88</td><td>0.575</td></tr><tr><td>10</td><td>10</td><td>14.142</td><td>45.0</td><td>133.0</td><td>133.0</td><td>551.6</td><td>551.6</td><td>289.1</td><td>25.22</td><td>3.93</td><td>0.578</td></tr><tr><td>16</td><td>0</td><td>16.000</td><td>0.0</td><td>213.8</td><td>0.0</td><td>897.5</td><td>0.0</td><td>411.4</td><td>30.67</td><td>3.73</td><td>0.584</td></tr><tr><td>15</td><td>8</td><td>17.000</td><td>28.1</td><td>201.0</td><td>107.2</td><td>850.1</td><td>453.4</td><td>502.4</td><td>34.38</td><td>3.38</td><td>0.588</td></tr><tr><td>18</td><td>1</td><td>18.028</td><td>3.2</td><td>242.0</td><td>13.4</td><td>1031.9</td><td>57.3</td><td>632.5</td><td>39.35</td><td>2.67</td><td>0.591</td></tr><tr><td>13</td><td>13</td><td>18.385</td><td>45.0</td><td>175.0</td><td>175.0</td><td>748.4</td><td>748.4</td><td>694.9</td><td>41.64</td><td>2.27</td><td>0.593</td></tr><tr><td>19</td><td>0</td><td>19.000</td><td>0.0</td><td>256.3</td><td>0.0</td><td>1102.1</td><td>0.0</td><td>869.1</td><td>47.79</td><td>1.01</td><td>0.596</td></tr></table>

The centers of the 1128 facets of the first mirror lie in a common plane at $z = Z _ { 1 } = 1 0 0 0 \ : \mathrm { m m }$ within a circle of radius 256.3 mm. The 1128 facets of the second mirror lie on a surface of revolution spanning $z _ { f } ( r ) = 2 . 0$ mm $( r = 1 )$ to 869.1 mm $( r = 1 9 )$ . Figure 15 shows a 3D rendering of the projection architecture. For clarity, the silver-colored backing of the second mirror is shown in the figure only to highlight the facets against its background. In the actual system, no such underlying surface exists.

Angles of incidence on mirror 1 range from $i _ { 1 } = 1 . 5 0 ^ { \circ } ~ ( r = 1 )$ to $4 7 . 7 9 ^ { \circ } \ ( r = 1 9 )$ , while on mirror 2 they remain between $i _ { 2 } = 0 . 3 7 ^ { \circ }$ and $3 . 9 3 ^ { \circ }$ . The two-reflection throughput $| R _ { 1 } R _ { 2 } |$ varies narrowly between 0.560 and 0.596 (mean $0 . 5 7 6 )$ , retaining ∼ 58% of the power leaving the mask in each selected order after the two reflections (4–20 times more than in 6–10-mirror schemes).

Practical limitations of the 3D case. The total of 2256 facets (1128 per mirror) makes direct fabrication and alignment technically challenging. However, due to rotational symmetry, 132 radial coating pairs are required, one per radial value $r ,$ corresponding to up to 264 distinct multilayer structures for the two mirrors rather than one design per facet. Replacing the second-mirror coatings by a common near-normal-incidence coating is a separate approximation.

![](images/cdad2883073391c4b5797ab911f92a46e090f516caf23d4af708210514d224eb.jpg)  
Figure 15: 3D CAD visualization of the all-reflective two-mirror system (viewed at $6 0 ^ { \circ }$ to the z-axis). Gray planar elements: 1128 facets of mirror 1 (in the plane $z = Z _ { 1 } = 1 0 0 0$ mm, disk radius 256.3 mm) and 1128 facets of mirror 2 (on the surface of revolution from $z _ { f } = 2$ mm to 869 mm). Red $1 \times 1$ cm squares denote the mask $( z = 0 )$ and wafer $\left( z = Z _ { 1 } \right)$ .

## 4.3 3D Mask Synthesis

## 4.3.1 Formulation of the 3D Inverse Problem

In 3D, all 1128 difraction orders have equal optical path lengths: $P _ { m , n } \approx 2 9 9 8 . 1$ mm. The difracted field contains two independent orthogonal transverse components, $E _ { x }$ and $E _ { y }$ , corresponding to scattering amplitudes $A _ { x ; m , n } ^ { ( r ) }$ and $A _ { y ; m , n } ^ { ( r ) }$ computed via the 3D waveguide method.

The harmonic amplitudes on the wafer are:

$$
\left[ \begin{array}{c} B _ {x; - m, - n} ^ {\mathrm{(w)}} \\ B _ {y; - m, - n} ^ {\mathrm{(w)}} \end{array} \right] = \hat {r} _ {2, m, n} \hat {r} _ {1, m, n} \left[ \begin{array}{c} A _ {x; m, n} ^ {(r)} \\ A _ {y; m, n} ^ {(r)} \end{array} \right], \qquad (m, n) \in \mathcal {D} _ {N},\tag{40}
$$

where $\hat { r } _ { 1 , m , n }$ and $\hat { r } _ { 2 , m , n }$ denote the complex matrix field reflection coeficients of the corresponding facets of the first and second mirrors for order $( m , n ) , \mathcal { D } _ { N } = \{ ( m , n ) \in \mathbb { Z } ^ { 2 } : m ^ { 2 } + n ^ { 2 } \leq N ^ { 2 } , ( m , n ) \neq ( 0 , 0 ) \}$ .

For the general vector transfer, each matrix acts on global transverse electric-field components and includes the local polarization bases,

$$
\hat {r} _ {j} = Q _ {j} ^ {\mathrm{out}} \operatorname{diag} (r _ {s, j}, r _ {p, j}) (Q _ {j} ^ {\mathrm{in}}) ^ {- 1}.
$$

The columns of $Q _ { j } ^ { \mathrm { i n } }$ and $Q _ { j } ^ { \mathrm { o u t } }$ are the xy projections of the incoming and outgoing local TE- and TMpolarization unit vectors, with the reflection coeficients defined in these same bases. The first reflection therefore acts before the second. The numerical demonstration retains the scalar-channel approximation with equal TE and TM coeficients and evaluates only transverse field components, as a proof-of-concept simplification.

The field components above the wafer are:

$$
\left[ \begin{array}{c} E _ {x} ^ {\mathrm{(w)}} (x, y) \\ E _ {y} ^ {\mathrm{(w)}} (x, y) \end{array} \right] = \sum_ {(m, n) \in \mathcal {D} _ {N}} \left[ \begin{array}{c} B _ {x; m, n} ^ {\mathrm{(w)}} \\ B _ {y; m, n} ^ {\mathrm{(w)}} \end{array} \right] \exp \bigl (- \mathrm{i} \kappa_ {x} ^ {\mathrm{(w)}} m x - \mathrm{i} \kappa_ {y} ^ {\mathrm{(w)}} n y \bigr),\tag{41}
$$

and the total aerial intensity is:

$$
I _ {\mathrm{w}} (x, y) = \left| E _ {x} ^ {(\mathrm{w})} (x, y) \right| ^ {2} + \left| E _ {y} ^ {(\mathrm{w})} (x, y) \right| ^ {2}.\tag{42}
$$

Although the incident wave is purely TE-polarized $\left( \mathbf { E } \parallel \mathbf { y } \right)$ , the 3D mask (with a two-dimensionally periodic structure $\varepsilon ( x , y ) )$ generates cross-polarized scattering, so that the scattering amplitude $A _ { x ; m , n } ^ { ( r ) }$ is non-zero (the incident field contains no cross-polarized component, $A _ { x ; m , n } ^ { ( i ) } = 0 )$

The 3D latent function is:

$$
f _ {\mathrm{latent}} (x, y) = \mathrm{Re} \left(\sum_ {m = - M} ^ {M} \sum_ {n = - M} ^ {M} F _ {m, n} \mathrm{e} ^ {- \mathrm{i} \kappa_ {x} m x - \mathrm{i} \kappa_ {y} n y}\right),\tag{43}
$$

where $F _ { m , n }$ are the complex Fourier coeficients to be optimized (the two-dimensional generalization of $F _ { m }$ in Eq. (25)). The physical absorber density is obtained via the sigmoid mapping $\rho ( x , y ) = \sigma ( \beta f _ { \mathrm { l a t e n t } } ) \in ( 0 , 1 )$ where β is a steepness parameter increased during optimization to enforce binarization, and σ is the sigmoid function defined in the 2D formulation. The permittivity is computed as $\varepsilon ( x , y ) = \varepsilon _ { \mathrm { v a c } } + \rho ( x , y ) ( \varepsilon _ { \mathrm { a b s } } - \varepsilon _ { \mathrm { v a c } } )$

## 4.3.2 Parameters and Results of Optimization

Parameters: $\lambda = 1 1 . 2$ nm, incidence angle $6 ^ { \circ } \ \left( \mathrm { T E } \right)$ , $L _ { x } = L _ { y } \approx 8 5 7$ nm, $L _ { x } ^ { \mathrm { ( w ) } } = L _ { y } ^ { \mathrm { ( w ) } } \approx 2 1 4$ nm, La absorber $( d _ { \mathrm { a b s } } = 6 0 ~ \mathrm { n m } )$ on $\mathrm { R u / B e / S r }$ Bragg mirror, Fourier expansion parameter $M _ { \mathrm { o p t } } \stackrel { \cdot } { = } M = 1 6$ (instead of the maximum propagating order $N = { \bar { 1 9 } } )$ , 500 epochs.

Figure 16 presents the optimization results: target emblem (University of Nizhny Novgorod logo), bandlimited target projection, continuous optimized absorber density $\rho ( x , y )$ ), synthesized aerial intensity, binarized mask, and aerial image from the binarized mask.

The binarization penalty ${ \mathcal { L } } _ { \mathrm { b i n } }$ drops from 0.25 to 0.002, and $\mathcal { L } _ { \mathrm { s h a p e } }$ decreases from $6 . 5 \times 1 0 ^ { - 8 }$ to $2 . 3 \times 1 0 ^ { - 8 }$ Truncating to $M = 1 6$ corresponds to $\mathrm { N A } = 0 . 8 4$

## 5 Discussion: Advantages and Disadvantages of the Proposed Projection System

## 5.1 Advantages

1. The array of $2 N = 3 8$ planar facets independently maps each mask difraction harmonic to the corresponding wafer harmonic up to $\mathrm { N A } _ { \mathrm { m a x } } = 0 . 9 9 3$ , a value unattainable in conventional multi-mirror EUV projection objectives with a limited number of reflections.

2. For the periodic structures considered here, the common illuminated wafer region can have an area comparable to the illuminated mask area, apart from edge efects. The unit-cell period is reduced by four along each transverse direction, so more repeated cells fit within the illuminated area. This does not imply demagnification of an arbitrary finite mask pattern while preserving its image area.

3. The finite facet apertures and angular selectivity of the Bragg coatings can act as spatial-frequency filters for individual channels. Suppression of unwanted angular components can reduce flare, but its efect on useful signal and aerial-image contrast requires a quantitative calculation with finite source bandwidth and angular extent, mask scattering, and facet acceptance.

4. The two reflections retain approximately 50–60% of the power leaving the mask in an accepted difraction order. This channel transmission is not the fraction of the total mask-reflected power or source power delivered to a useful image region. Comparison values of about 12% for six reflections and 2.8% for ten reflections refer only to products of mirror reflectances.

5. Each accepted harmonic undergoes the spatial-frequency transformation $m \kappa _ { x }  - 4 m \kappa _ { x }$ , corresponding to fourfold reduction and inversion of the periodic coordinate. Order-dependent complex reflection coeficients and aperture truncation modify the pattern, so exact reproduction of its shape is not implied by the linear frequency map alone.

6. In Examples 1 and 2, all N beams propagate strictly parallel to the z-axis after the first reflection, simplifying mutual alignment. In Example 3, beams propagate at deflection angles $( \theta _ { m } ^ { \mathrm { ( w ) } } - \theta _ { m } )$ ranging from $\sim 2 ^ { \circ } \ \mathrm { t o } \sim 6 9 ^ { \circ }$ , and in Example 4 at tailored angles $\beta _ { m }$

Optimized absorber

Binarized absorber  
![](images/3946f9c7bdb6c7ada56d310db8f832ab925f0e22651d53f3b96e73c918163204.jpg)

![](images/09071fe143553df7c8fdd7c62aed15d853f4e9eee282a6f301a7789c88cfef98.jpg)

![](images/b8dd3ce6569db91e10353bdfbd817cca824dfb41211cbbeec734db3d4cb032d8.jpg)

![](images/35fd5190975e70d78e2c7daf4df44d57ade4a362419ab0fda882459915a72882.jpg)  
x (nm)

![](images/ee85450cd0331592894b70842eff9d29fa0e5780a1b0c08fd3b0e576b7f16711.jpg)  
x (nm)

![](images/98c511ceb239ea886cd1ea590214a3380ff0cf1945ef396cdd767c7073d7e6f4.jpg)  
x (nm)  
Figure 16: Optimization results for a 3D mask in the projection system $( \lambda = 1 1 . 2 \mathrm { n m }$ , La absorber, $M _ { \mathrm { o p t } } = 1 6$ $\mathrm { N } \bar { \mathrm { A } } \approx 0 . 8 4$ , 500 epochs). Top row: target image (UNN logo), target projection onto propagating harmonics, optimized absorber density $\rho ( x , y )$ . Bottom row: synthesized aerial intensity on the wafer, binarized mask $\left( \rho > \langle \rho \rangle \right)$ , aerial intensity from the binarized mask. The mask period is $L _ { x } = \dot { L } _ { y }$ ≈ 857 nm. The wafer period is $L _ { x } ^ { \mathrm { ( w ) } } \approx 2 1 4$ nm.

7. In Examples 1 and 2, tilt angles of the first mirror do not exceed $7 . 2 ^ { \circ }$ , rendering it nearly planar and amenable to precision machining with sub-micrometer accuracy. In Example 3, tilt angles reach $2 7 . 2 ^ { \circ }$ , and in Example 4, 33.4<sup>◦</sup>.

8. All facets are planar, so Bragg coatings can be laterally homogeneous across each facet, eliminating the complex graded-layer deposition required on aspheric surfaces in conventional systems [7].

9. Separate facet pairs permit channel-specific coating optimization and can allow modular changes to the accepted numerical aperture and local replacement of degraded elements. Their practical benefit depends on alignment, phase control, and thermal and mechanical stability. Replacement without optical readjustment has not been demonstrated.

## 5.2 Disadvantages

1. Changing $L _ { x }$ or $L _ { y }$ changes the difraction angles and can require new facet positions, tilts, coatings, and channel counts. Feasibility depends on the available mechanical clearance, optical acceptance, phase tolerances, and source bandwidth. It is not established for arbitrary periods.

2. Projections of the beams on the wafer grow as $L _ { m } ^ { \mathrm { ( w ) } } = a _ { m } / \cos \theta _ { m } ^ { \mathrm { ( w ) } }$ : values remain below 18 mm for $m \leq 1 6$ , reach 28.7 mm for $m = 1 8$ , and 82.1 mm for $m = 1 9$ (at $\theta _ { 1 9 } ^ { ( \mathrm { w ) } } = 8 3 . 2 ^ { \circ }$ , the projection is stretched by a factor of 8.5). This is not related to difractive beam spreading but is a geometric consequence of the grazing projection of a finite-width beam $( a _ { m } \approx 1 0$ mm) onto the wafer plane. The efect can be mitigated by apodization or by sizing the apertures of the high-order facets.

3. In Example 2, the second-mirror facets operate at grazing angles from $1 . 5 ^ { \circ }$ to 41.6<sup>◦</sup>. The facet length required for full beam interception reaches 382.5 mm for $m = 1$ , whereas the corresponding lengths in Example 4 are approximately 10 mm.

4. In Example 4, the first-mirror facet centers span ±256.3 mm, while the second-mirror centers reach ±1102.1 mm. The complete transverse span is therefore approximately 2204.2 mm using the rounded tabulated coordinates, before mechanical supports and facet extents are included. The total optical path length is approximately 3 m.

5. Preserving the energy balance across difraction harmonics requires individual optimization of Bragg bilayer thicknesses for each first-mirror facet, covering incidence angles from $1 . { \dot { 5 } } ^ { \circ }$ to 47.8<sup>◦</sup>.

6. The optical path diferences in Examples 1–3 introduce deterministic relative propagation phases, rather than destroying coherence under strictly monochromatic illumination. Example 4 removes these path-dependent phase diferences. Position tolerances must be set by the allowable wavefront error, while a finite source bandwidth additionally requires temporal-coherence analysis.

7. A normal surface displacement δh produces an optical-path error of approximately 2δh cos i. For independent errors on two nearly normally reflecting facets, σ<sub>P</sub> ≈ $2 \sqrt { 2 } \sigma _ { h }$ . As an illustrative wavefront criterion, $S \approx \exp \left[ - ( 2 \pi \sigma _ { P } / \lambda ) ^ { 2 } \right] \geq 0 . 8$ at $\lambda = 1 1 . 2$ nm gives $\sigma _ { h } \lesssim 0 . 3 0$ nm per facet. The actual surface and alignment tolerances must be derived from the aerial-image requirements and error correlations, especially across 2256 facets.

8. The validity of treating difraction orders as bounded collimated beams is analyzed in Appendix A, confirming high precision for centimeter-scale EUV beams.

## 6 Conclusion

In this work, an all-reflective EUV projection concept has been proposed and investigated that uses two reflections per accepted channel between the mask and wafer, with each mirror composed of individual planar facets corresponding to each spatial difraction order.

The main conclusions are:

1. A two-mirror projection concept providing 4× reduction of the periodic unit cell at $\mathrm { N A } _ { \mathrm { m a x } } \approx 0 . 9 9 3$ is analyzed at 13.5 nm and 11.2 nm, with $L _ { x } / \lambda$ kept fixed.

2. A spatial geometry providing rigorous equalization of optical path lengths across all difraction harmonics is established, removing order-dependent propagation phase shifts.

3. Multi-parameter optimization of 30-bilayer Bragg mirrors (Mo/Si at 13.5 nm and Ru/Be at 11.2 nm) demonstrates channel throughput of ∼ 51–60%. Facets of the second mirror operate at quasi-normal incidence (≤ 3.93<sup>◦</sup>) suggesting the possibility of a common coating as a separate approximation.

4. The concept is generalized to 3D periodic masks. It has been shown that for the considered mask, the 2256-facet system with 1128 selected orders requires optimizing 132 radial coating pairs, or up to 264 distinct multilayer structures, due to rotational symmetry.

5. Inverse lithography produces simulated aerial images with a central peak of approximately 5.4 nm FWHM from a 4.6-nm-wide target and with two 6-nm-wide target lines separated by 6 nm. The unused back-reflection order is suppressed in the 2D optimization, and the two peaks remain resolved for the tested defocus values up to 5 nm. Resist printing and a full process window have not been evaluated.

6. The validity of the geometrical-optics beam approximation for centimeter-scale EUV beams over ∼ 1 m paths is proven (collimation length exceeds hundreds of meters, and edge blur is under a millimeter).

The modular faceted approach ofers a route to reducing the number of reflections in periodic-pattern projection while using planar reflecting surfaces. Its applicability to high-resolution lithography requires further assessment of source coherence and bandwidth, polarization, fabrication and alignment tolerances, and resist response. This faceted approach can removes the fundamental technological constraints of multi-mirror EUV optics associated with the number of reflections and complex aspherization, opening a promising route toward projection lithography systems of ultra-high resolution (NA → 1).

## A Difractive Propagation of a Hard-Apertured Beam

## A.1 Problem Formulation

As in the main text, the time dependence $\exp ( \mathrm { i } \omega t )$ is assumed and omitted. Let the initial field at $z = 0$ be non-zero only over an aperture of width W along x:

$$
E (x, 0) = E _ {0}   \Pi \Bigl (\frac {x}{W} \Bigr)   \mathrm{e} ^ {- \mathrm{i} k _ {x} x}, \qquad \Pi (u) = \left\{ \begin{array}{l l} 1, & | u | \leq 1 / 2, \\ 0, & | u | > 1 / 2, \end{array} \right.\tag{44}
$$

where $k _ { x }$ is the transverse wavevector component:

$$
\mathbf {k} = (k _ {x}, 0, k _ {z}), \qquad k _ {x} ^ {2} + k _ {z} ^ {2} = k _ {0} ^ {2}, \qquad k _ {0} = \frac {2 \pi}{\lambda}.\tag{45}
$$

The propagation angle relative to the z-axis is $\alpha = \arcsin ( k _ { x } / k _ { 0 } ) \ : ( \cos \alpha = k _ { z } / k _ { 0 } )$

## A.2 Angular Spectrum

Expanding Eq. (44) into plane waves:

$$
E (x, z) = \int_ {- \infty} ^ {\infty} A (q) \mathrm{e} ^ {- \mathrm{i} q x - \mathrm{i} \gamma (q) z} \frac {\mathrm{d} q}{2 \pi}, \quad \gamma (q) = \left(k _ {0} ^ {2} - q ^ {2}\right) ^ {1 / 2}, \quad \operatorname{Im} \gamma (q) \leq 0,\tag{46}
$$

with spectral amplitude:

$$
A (q) = E _ {0} W \operatorname{sinc} \left[ \frac {(q - k _ {x}) W}{2} \right], \quad \operatorname{sinc} u \equiv \frac {\sin u}{u}.\tag{47}
$$

The spectral half-width to first zeros is $\Delta q = 2 \pi / W$ . The divergence half-angle is:

$$
\theta_ {0} = \frac {\Delta q}{k _ {0} \cos \alpha} = \frac {\lambda}{W \cos \alpha} = \frac {\lambda k _ {0}}{W k _ {z}} = \frac {\lambda}{W _ {\perp}},\tag{48}
$$

governed by the perpendicular beam width:

$$
W _ {\perp} = W \cos \alpha = \frac {W k _ {z}}{k _ {0}}.\tag{49}
$$

## A.3 Paraxial Approximation and Beam Coordinate System

Using the beam coordinates $( \xi , \zeta )$ defined below, write $E ( x , z ) = \exp ( - \mathrm { i } k _ { 0 } \zeta ) U ( \xi , \zeta )$ . Neglecting $\partial ^ { 2 } U / \partial \zeta ^ { 2 }$ relative to $2 \mathrm { i } k _ { 0 } \partial U / \partial \zeta$ gives the paraxial envelope equation

$$
2 \mathrm{i} k _ {0} \frac {\partial U}{\partial \zeta} = \frac {\partial^ {2} U}{\partial \xi^ {2}}.\tag{50}
$$

Equation (50) describes difraction along the beam axis. In laboratory coordinates, an envelope extracted using $\exp [ - \mathrm { i } ( k _ { x } x + k _ { z } z ) ]$ also has a transverse transport term. The spectral curvature is $\gamma ^ { \prime \prime } ( k _ { x } ) = - k _ { 0 } ^ { 2 } / k _ { z } ^ { 3 }$ In the beam coordinate frame $( \xi , \zeta )$

$$
\zeta = x \sin \alpha + z \cos \alpha \quad (\text { along   the   beam   axis }), \qquad \xi = x \cos \alpha - z \sin \alpha \quad (\text { transverse   to   the   beam }).\tag{51}
$$

Along the central ray, a propagation distance z in the laboratory frame corresponds to $\zeta = z / \cos \alpha = z k _ { 0 } / k _ { z }$ along the beam axis.

To leading paraxial order, the oblique aperture is represented on the transverse beam plane by a top-hat envelope of width $W _ { \perp }$ . Its propagation is described by the Fresnel integral

$$
U (\xi , \zeta) = \sqrt {\frac {k _ {0}}{- 2 \pi \mathrm{i} \zeta}} \int_ {- W _ {\perp} / 2} ^ {W _ {\perp} / 2} U (\xi^ {\prime}, 0) \exp \left[ - \frac {\mathrm{i} k _ {0} (\xi - \xi^ {\prime}) ^ {2}}{2 \zeta} \right] \mathrm{d} \xi^ {\prime}.\tag{52}
$$

## A.4 Key Difraction Scales

From Eq. (52), three characteristic scales emerge (where $L \equiv \zeta$ is propagation distance):

1. Fresnel number $( N _ { F } )$ and collimation length $( L _ { F } ) .$

$$
N _ {F} (L) = \frac {(W _ {\perp} / 2) ^ {2}}{\lambda L} = \frac {L _ {F}}{L}, \qquad L _ {F} = \frac {W _ {\perp} ^ {2}}{4 \lambda} = \frac {W ^ {2} k _ {z} ^ {2}}{4 k _ {0} ^ {2} \lambda}.\tag{53}
$$

Near-field geometrical propagation holds for $N _ { F } \gg 1$ , while Fraunhofer difraction occurs for $N _ { F } \ll 1$

2. Near-Field Boundary Blur: The edge transition scale is:

$$
\Delta \sim \sqrt {\lambda L} = \sqrt {\frac {2 \pi L}{k _ {0}}},\tag{54}
$$

with the 10%–90% intensity transition width given by:

$$
\Delta_ {10 - 90\%} \approx 0.829 \sqrt {\lambda L}.\tag{55}
$$

3. Far-Field Divergence: The angular intensity profile is:

$$
I (\theta) = I _ {0} \operatorname{sinc} ^ {2} \left(\frac {\pi W _ {\perp} \theta}{\lambda}\right),\tag{56}
$$

with a main-lobe angular width between the first zeros of $2 \theta _ { 0 } = 2 \lambda / W _ { \perp }$ , a full width at half maximum of FWHM $\approx 0 . 8 8 6 \lambda / W _ { \perp }$ , and a first sidelobe of $\approx 4 . 7 \%$ of the maximum. The beam size expands as $D ( L ) \approx 2 \theta _ { 0 } L$

## A.5 Near-Field Boundary Structure

When $\sqrt { \lambda L } \ll W _ { \perp } \left( N _ { F } \gg 1 \right)$ , opposite aperture edges difract independently, matching semi-infinite knife-edge difraction:

$$
I (v) = \frac {I _ {0}}{2} \left\{\left[ C (v) + \frac {1}{2} \right] ^ {2} + \left[ S (v) + \frac {1}{2} \right] ^ {2} \right\}, \qquad v = (\xi_ {\mathrm{edge}} - \xi) \sqrt {\frac {2}{\lambda L}},\tag{57}
$$

where $C ( v )$ and $S ( v )$ are Fresnel integrals and $\xi _ { \mathrm { e d g e } }$ is the right aperture edge, so $v > 0$ points into the illuminated region. Characteristics include:

• At the shadow boundary, $I ( 0 ) = I _ { 0 } / 4$

• The first difraction peak reaches I ≈ 1.37 $I _ { 0 }$ at v ≈ 1.22.

• In the illuminated region, decaying Fresnel fringes occur with period $\sim \lambda L / | \xi - \xi _ { \mathrm { e d g e } } |$

• Field decays monotonically into the shadow region.

The number of Fresnel oscillations across the beam width is of the order of $N _ { F }$ . As $N _ { F }$ decreases $\mathrm { t o } \sim 1 0$ the oscillations from the opposite edges begin to interfere with each other, distorting the central part of the plateau. At $N _ { F } \sim 1$ the profile smooths out and transitions into the far-field distribution (56).

A.6 Numerical Example: $\lambda = 1 1 . 2$ nm, $W = 1$ cm, $k _ { x } = k _ { z }$

For $k _ { x } = k _ { z } = k _ { 0 } / \sqrt { 2 } \ ( \alpha = 4 5 ^ { \circ } )$ :

<table><tr><td>Parameter</td><td>Value</td></tr><tr><td> $k_0 = 2\pi/\lambda$ </td><td> $5.61 \times 10^{8} \text{ m}^{-1}$ </td></tr><tr><td> $k_x = k_z$ </td><td> $3.97 \times 10^{8} \text{ m}^{-1}$ </td></tr><tr><td> $W_\perp = W/\sqrt{2}$ </td><td> $7.07 \text{ mm}$ </td></tr><tr><td> $\theta_0 = \lambda/W_\perp$ </td><td> $1.58 \times 10^{-6} \text{ rad} \approx 0.33''$ </td></tr><tr><td> $L_F = W_\perp^2/(4\lambda)$ </td><td> $1.1 \times 10^{3} \text{ m}$ </td></tr></table>

Table 8 and Figs. 17–19 illustrate beam evolution across distances.

Table 8: Difractive beam evolution with propagation distance $( \lambda = 1 1 . 2 \ \mathrm { n m } , W _ { \perp } = 7 . 0 7 \ \mathrm { m m } )$ . The 10%–90% widths at $L \leq 1 0 0$ m use the independent-edge approximation. The $L = 1 0 0 0$ m value is a numerical finite-slit estimate, where the two edge fields overlap and Eq. (55) is not applicable.

<table><tr><td>L, m</td><td> $N_{F}$ </td><td> $\sqrt{\lambda L}$  (mm)</td><td> $\Delta_{10-90\%}$  (mm)</td><td>Propagation Regime</td></tr><tr><td>1</td><td>1116</td><td>0.11</td><td>0.09</td><td>Geometrical shadow</td></tr><tr><td>10</td><td>112</td><td>0.33</td><td>0.28</td><td>Near field</td></tr><tr><td>100</td><td>11</td><td>1.06</td><td>0.88</td><td>Edge-ripple overlap</td></tr><tr><td>1000</td><td>1.1</td><td>3.35</td><td>2.30</td><td>Intermediate zone</td></tr><tr><td>10000</td><td>0.11</td><td>10.6</td><td>—</td><td>Fraunhofer far field (FWHM = 14 mm)</td></tr></table>

![](images/847509e524c19e27740dd570f239d429b8effa08b527ed76998acb08dfabe8eb.jpg)

![](images/c9252a6d4411752949015fdaf46f68fe8569e71af5886df011361eed400bfe4e.jpg)

![](images/a0ca158a0bd5981877b00e8a27f3ee1b32d790a0e27cbe988e4efbc3f17e805d.jpg)

![](images/bd35a10670862b4595314d1c7a816c688c34f839c39379ea40975eda0a59a18f.jpg)

![](images/6a7a66a571ec490f8b823c4fb06e080e17f47fad7736432d06bf784d5e0b988c.jpg)  
Figure 17: Transverse intensity profile evolution versus distance (angular spectrum calculation). Dashed lines: geometrical shadow boundaries.

## A.7 Conclusions of the Difraction Analysis

1. A centimeter-aperture EUV beam $( W _ { \perp } \approx 7 ~ \mathrm { m m } )$ at $\lambda = 1 1 . 2$ nm exhibits high collimation stability: $L _ { F } \approx 1 . 1$ km and divergence $\theta _ { 0 } \approx 1 . 6$ µrad. Over typical optical paths $( L \sim 1 \bar { - } 3 ~ \mathrm { m } )$ , the beam profile is practically indistinguishable from the geometrical projection of the mask.

2. Edge blur obeys $\Delta \sim \sqrt { \lambda L } ,$ amounting to only 0.09 mm at 1 m and 0.28 mm at 10 m. Near the boundaries, Fresnel fringes form with a local peak reaching 1.37 $I _ { 0 } ,$ decaying monotonically into the shadow.

3. At distances $L \gtrsim L _ { F } ,$ , sharp edges blur and the beam transitions into a $\mathrm { s i n c ^ { 2 } }$ distribution with sidelobe levels $\mathrm { o f } \approx 4 . 7 \%$ . The beam diameter grows linearly $( D \approx 2 \theta _ { 0 } L )$

4. Hard aperture truncation generates edge ripples. If suppression is required, apodizing elements with smoothed edge transmission/reflection can be incorporated.

![](images/bbd025e0051e7b502a262737e7825ac9adef2e0bf1c193f58b204140a28c6e80.jpg)  
Figure 18: Right-edge boundary difraction profile. The solid line shows the slit calculation. The dashed line shows the semi-infinite knife-edge analytical model, Eq. (57). Small oscillations at $L = 1 0 0$ m arise from interference with the wave difracted by the opposite edge.

![](images/7ca6c767f429f9d597272355a897f704a039734a568aed8cafcb9f3676654f2a.jpg)  
Figure 19: Far-field intensity distribution $( L = 1 0$ km, $N _ { F } = 0 . 1 1 )$ : the solid line shows the numerical result in normalized angular coordinate $\theta / \theta _ { 0 }$ . The dashed line shows the theoretical sin $\mathsf { z } ^ { 2 } ( \pi W _ { \perp } \theta / \lambda )$

## B Nomenclature

This table summarizes the main abbreviations used in the paper.

Table 9: Nomenclature

<table><tr><td>Notation</td><td>Description</td></tr><tr><td>CAD</td><td>Computer-aided design</td></tr><tr><td>CD</td><td>Critical dimension</td></tr><tr><td>DoF</td><td>Depth of focus</td></tr><tr><td>EUV</td><td>Extreme ultraviolet</td></tr><tr><td>FWHM</td><td>Full width at half maximum</td></tr><tr><td>GO</td><td>Geometrical optics</td></tr><tr><td>ILT</td><td>Inverse lithography technology</td></tr><tr><td>L-BFGS-B</td><td>Bound-constrained limited-memory BFGS method</td></tr><tr><td>Mo/Si</td><td>Molybdenum/silicon multilayer Bragg coating</td></tr><tr><td>MSE</td><td>Mean squared error</td></tr><tr><td>NA</td><td>Numerical aperture</td></tr><tr><td>OAI</td><td>Off-axis illumination</td></tr><tr><td>RCWA</td><td>Rigorous coupled-wave analysis</td></tr><tr><td>RMS</td><td>Root mean square</td></tr><tr><td>Ru/Be</td><td>Ruthenium/beryllium multilayer Bragg coating</td></tr><tr><td>Ru/Be/Sr</td><td>Ruthenium/beryllium/strontium multilayer Bragg coating</td></tr><tr><td>TE</td><td>Transverse electric polarization</td></tr><tr><td>TM</td><td>Transverse magnetic polarization</td></tr><tr><td>TMM</td><td>Transfer-matrix method</td></tr><tr><td>HF</td><td>High-frequency penalty</td></tr><tr><td>UNN</td><td>University of Nizhny Novgorod</td></tr></table>

## References

[1] J. van Schoot, R. van Ballegoij, H. Butler, E. van Setten, G. Schifelers, W. Bouman, S. van Gorp, K. Umstadter, J. Zimmermann, D. Golde, J. T. Neumann, and P. Graeupner, “Next step in Moore’s law: high NA EUV system overview and first imaging and overlay performance,” J. Micro/Nanopattern. Mater. Metrol., vol. 24, no. 1, p. 011009, 2025, doi: 10.1117/1.JMM.24.1.011009.

[2] N. I. Chkhalo, “New Concept for the Development of High-Performance X-ray Lithography,” Russian Microelectronics, vol. 53, no. 5, pp. 397–407, oct 2024. [Online]. Available: https: //link.springer.com/10.1134/S1063739724600511

[3] IEEE IRDS, “International roadmap for devices and systems (IRDS): 2024 update, More Moore,” IEEE, Tech. Rep., 2024. [Online]. Available: https://irds.ieee.org/

[4] N. I. Chkhalo, S. A. Gusev, A. N. Nechay, D. E. Pariev, V. N. Polkovnikov, N. N. Salashchenko, F. Schäfers, M. G. Sertsu, A. Sokolov, M. V. Svechnikov, and D. A. Tatarsky, “High-reflection mo/be/si multilayers for euv lithography,” Opt. Lett., vol. 42, no. 24, pp. 5070–5073, Dec 2017. [Online]. Available: https://opg.optica.org/ol/abstract.cfm?URI=ol-42-24-5070

[5] M. van de Kerkhof, A. Klein, P. Vermeulen, T. van der Woord, I. Donmez, G. Salmaso, and R. Maas, “High-transmission EUV pellicles supporting >400W source power,” in Proc. SPIE, vol. 12051, 2022, p. 120510B, optical and EUV Nanolithography XXXV; doi: 10.1117/12.2614262.

[6] J. van Schoot, E. van Setten, G. Rispens, K. Z. Troost, B. Kneer, S. Migura, J. T. Neumann, and W. Kaiser, “High-numerical aperture extreme ultraviolet scanner for 8-nm lithography and beyond,” J. Micro/Nanolith. MEMS MOEMS, vol. 16, no. 4, p. 041010, 2017, doi: 10.1117/1.JMM.16.4.041010.

[7] J. Kalden, J. T. Neumann, D. Jürgens, P. Gräupner, W. Seitz, and P. Kürz, “EUV optics at ZEISS: status, outlook, and future,” in Proc. SPIE, vol. 12953, 2024, p. 129530Q, optical and EUV Nanolithography XXXVII.

[8] E. van Setten, G. Bottiglieri, L. de Winter, J. McNamara, P. Rusu, J. Lubkoll, G. Rispens, and J. van Schoot, “Edge placement error control and Mask3D efects in High-NA anamorphic EUV lithography,” in Proc. SPIE, vol. 10450, 2017, p. 104500W, doi: 10.1117/12.2280624.

[9] T. Shintake, “Can we improve the energy eficiency of EUV lithography?” arXiv preprint arXiv:2405.11717, 2024, presented at the Photomask Japan Symposium, Yokohama, Japan.

[10] I. Abramov, S. Golubev, E. Gospodchikov, A. Shalashov, A. Perekalov, A. Nechay, and N. Chkhalo, “Laser discharge in a high-pressure jet of heavy noble gas: Expansion of emitting volume promises an eficient source of euv light for lithography,” Phys. Rev. Appl., vol. 23, p. 024004, Feb 2025. [Online]. Available: https://link.aps.org/doi/10.1103/PhysRevApplied.23.024004

[11] R. A. Shaposhnikov, V. N. Polkovnikov, N. N. Salashchenko, N. I. Chkhalo, and S. Y. Zuev, “Highly reflective ru/sr multilayer mirrors for wavelengths 9–12 nm,” Opt. Lett., vol. 47, no. 17, pp. 4351–4354, Sep 2022. [Online]. Available: https://opg.optica.org/ol/abstract.cfm?URI=ol-47-17-4351

[12] V. N. Polkovnikov, N. N. Salashchenko, M. V. Svechnikov, and N. I. Chkhalo, “Beryllium-based multilayer x-ray optics,” Physics-Uspekhi, vol. 63, no. 1, p. 83, jan 2020. [Online]. Available: https://doi.org/10.3367/UFNe.2019.05.038623

[13] T. Shintake, “High-NA in-line projector for EUV lithography,” arXiv preprint arXiv:2508.00433, 2025, oIST; JPN Patent Application 2025-119190.

[14] H. Fukuda and T. Terasawa, “Design and analysis of difraction mirror optics for EUV projection lithography,” Microelectronic Engineering, vol. 27, pp. 239–242, 1995.

[15] Z. Zheng, X. Sun, P. Gu, and X. Liu, “Design of objective lens with reflective spherical Fresnel zone plate,” Frontiers of Optoelectronics in China, vol. 1, no. 1–2, pp. 178–182, 2008.

[16] Z. Zheng, “Design of of-axis reflective projection lens using spherical Fresnel surface,” Optik, vol. 122, pp. 145–149, 2011.

[17] N. Choksi, D. S. Pickard, M. McCord, R. F. W. Pease, Y. Shrof, Y. Chen, W. Oldham, and D. Markle, “Maskless extreme ultraviolet lithography,” Journal of Vacuum Science & Technology B, vol. 17, no. 6, pp. 3047–3051, 1999.

[18] B. Henke, E. Gullikson, and J. Davis, “X-ray interactions: Photoabsorption, scattering, transmission, and reflection at e = 50-30,000 ev, z = 1-92,” Atomic Data and Nuclear Data Tables, vol. 54, no. 2, pp. 181–342, 1993. [Online]. Available: https://www.sciencedirect.com/science/article/pii/S0092640X83710132

[19] Center for X-Ray Optics. Lawrence Berkeley National Laboratory. (1993–2025) Index of refraction. [Online]. Available: https://henke.lbl.gov/optical\_constants/getdb2.html

[20] V. A. Es’kin and E. V. Ivanov, “Physics-informed neural systems for the simulation of euv electromagnetic wave difraction from a lithography mask,” 2026. [Online]. Available: https://arxiv.org/abs/2603.15584

[21] H. Tanabe, A. Jinguji, and A. Takahashi, “Accelerating extreme ultraviolet lithography simulation with weakly guiding approximation and source position dependent transmission cross coeficient formula,” Journal of Micro/Nanopatterning, Materials, and Metrology, vol. 23, no. 1, pp. 014 201–014 201, 2024.

[22] C.-M. Yuan and A. J. Strojwas, “Modeling optical microscope images of integrated-circuit structures,” Journal of the Optical Society of America A, vol. 8, no. 5, pp. 778–790, 1991.

[23] K. D. Lucas, H. Tanabe, and A. J. Strojwas, “Eficient and rigorous three-dimensional model for optical lithography simulation,” Journal of the Optical Society of America A, vol. 13, no. 11, pp. 2187–2199, 1996.

[24] V. Medvedev, A. Erdmann, and A. Roßkopf, “3d mask simulation and lithographic imaging using physics-informed neural networks,” 2023. [Online]. Available: https://publica.fraunhofer.de/handle/ publica/450903

[25] V. A. Es’kin and E. V. Ivanov, “Physics-informed neural networks and neural operators for a study of euv electromagnetic wave difraction from a lithography mask,” in 2025 Days on Difraction (DD), 2025, pp. 48–53.

[26] V. A. Es’kin and E. V. Ivanov, “Gradient-based inverse lithography for euv masks via the waveguide method and a physics-informed neural operator,” 2026. [Online]. Available: https://arxiv.org/abs/2606.25753