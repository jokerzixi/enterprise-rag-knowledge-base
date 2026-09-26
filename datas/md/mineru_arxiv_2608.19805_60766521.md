# Controlling catalyst agglomeration in high-density unordered III-V nanowire growth using Au colloid solutions

Chris Yannic Bohlemann,†<sup>,</sup>‡ Pavithira Manoharan,†<sup>,</sup>‡ Helene Reichel,† Kai Daniel

Hanke,† Peter Kleinschmidt,† Thomas Hannappel,† and Juliane Koch∗<sup>,</sup>†<sup>,</sup>‡

Technische Universit¨at Ilmenau, Fundamentals of Energy Materials & Institute for Micro-

and Nanotechnology, Postbox 100 565, D-98693 Ilmenau

Technische Universit¨at Ilmenau, CZS Junior Research Group for substitution and

recycling strategies for solar energy materials, Postbox 100 565,D-98693 Ilmenau

E-mail: j.koch@tu-ilmenau.de

## Abstract

III-V semiconductor nanowires (NWs) are a promising platform for optoelectronic and photoelectrochemical applications, where device performance strongly depends on NW density and spatial arrangement. While ordered arrays provide precise control, their fabrication requires complex and costly lithographic techniques. Unordered growth ofers a scalable alternative but is limited by insuficient control over catalyst distribution and particle agglomeration.

Here, we investigate the density scaling of unordered III-V NW arrays using commercially available Au colloid solutions as catalysts for NW growth via vapor-liquidsolid growth mode. Repeated deposition cycles yield a near-linear increase in particle density, which is ultimately limited by non-linear agglomeration efects not captured by simple stochastic models.

To address this limitation, a previously established pre-anneal growth concept is transferred from patterned catalyst arrays to randomly deposited Au colloids, thereby suppressing thermally induced coalescence and stabilizing the catalyst distribution. This approach enables up to a tenfold increase in NW density while improving uniformity and vertical yield. The method is demonstrated for colloid diameters between 100 and 200 nm.

Overall, this work provides a scalable, lithography-free route toward high-density III-V NW ensembles and ofers insight into the role of particle dynamics in colloid-based growth processes.

## 1 Introduction

Over the past decades, semiconductor nanowires (NWs) have emerged as a versatile platform for optoelectronic devices due to their quasi-one-dimensional geometry, which enables eficient charge carrier confinement, short transport paths, and pronounced surface interactions. These properties make NWs promising for applications in photodetectors, <sup>1–4</sup> light-emitting devices,<sup>5–7</sup> chemical sensors,<sup>8–10</sup> and photoelectrochemical systems.<sup>11–13</sup>

Their high surface-to-volume ratio, combined with geometry-dependent optical efects such as light trapping and enhanced absorption,<sup>14,15</sup> further strengthens light-matter interaction and positions NW arrays as an eficient architecture for energy conversion structures. Among available material systems, III-V semiconductor materials are particularly attractive due to their tunable band gaps, high charge carrier mobility, and controllable doping.<sup>16–18</sup> In NW geometries, elastic strain can relax laterally, enabling the integration of lattice-mismatched materials with significantly reduced defect densities compared to planar thin films.<sup>19</sup> This opens a pathway for the monolithic integration of high-performance III-V materials on silicon substrates, supporting scalable and cost-efective device fabrication.<sup>20,21</sup>

However, device performance is highly sensitive to NW geometry and array configuration including NW density, uniformity, and spatial arrangement. Numerical studies indicate that optimal absorption is material dependent and typically achieved for III-V NW lengths exceeding 2 µm and diameters ranging from 140 nm (InP) to 180 nm (GaAs). <sup>22–25</sup> In addition, the ratio between inter-wire distance, which is also known as pitch, and NW diameter is a critical parameter, with optimal pitch-to-diameter ratios of 0.4 to 0.5 for GaAs, <sup>23–26</sup> and lower ratios of 0.2 to 0.4 for In-based systems. <sup>22,27,28</sup> Because NW density scales inversely with the square of the array pitch, these constraints correspond to target densities of approximately $2 { \times } 1 0 ^ { 8 } \ \mathrm { N W / c m ^ { 2 } }$ for InP NW arrays and up to 8 10<sup>8</sup> NW/cm<sup>2</sup> for GaAs NW arrays. Achieving such densities is therefore essential for maximizing optical absorption.

Realizing these geometrically optimized NW arrays requires precise and scalable fabrication strategies. In general, NWs can be fabricated using either top-down or bottom-up approaches.<sup>29</sup> Top-down methods rely on lithography and subsequent etching to define NW structures with high positional accuracy, <sup>30</sup> enabling horizontally or vertically aligned NWs architectures.<sup>31,32</sup> However, these often sufer from surface roughness and etching-induced defects that can degrade optical and electronic performance. <sup>33,34</sup> In contrast, bottom-up approaches ofer superior material quality and improved material eficiency. <sup>16,31,33</sup> Among these, particle-assisted growth based on the vapor-liquid-solid (VLS) mechanism is widely employed,<sup>9,29,33</sup> where metallic catalyst particles determine the NW diameter and nucleation site. Especially for GaAs NWs, Au-based catalysts play an active role in the growth process by collecting growth species and forming an Au–Ga-rich phase at the NW growth front, thereby promoting precursor incorporation and axial crystal growth.<sup>35–38</sup> A key distinction within bottom-up fabrication lies between ordered arrays and unordered NW ensembles.<sup>15,33</sup> Ordered arrays can for example be fabricated using electron beam lithography <sup>39,40</sup> or nano imprint lithography, <sup>41,42</sup> provide precise control over position and geometry, enabling reproducible device characteristics and facilitating simplified modeling. However, they typically rely on complex and costly lithographic processing. <sup>15,31</sup> In contrast, unordered growth routes relying on depositing colloidal Au nanoparticles <sup>43,44</sup> or thermally dewetting Au thin films,<sup>45,46</sup> ofer a simpler and more cost-efective fabrication route, but generally results in reduced control over NW uniformity and spatial distribution.<sup>47</sup> Colloidal Au nanoparticles are particularly attractive for GaAs NW growth because they provide a simple and inexpensive fabrication route together with well-defined catalyst diameters and, consequently, good control over the initial NW diameter. <sup>43,44</sup> However, reproducible control of catalyst density and spatial distribution remains challenging, since deposition, agglomeration, and thermally induced particle motion on GaAs can modify the initially deposited particle ensemble.<sup>44,48</sup> This often leads to lower achievable densities and limits the exploitation of collective optical efects.<sup>49,50</sup> Systematic studies on achievable NW densities in unordered particle-assisted growth, particularly for colloid diameters above 100 nm, remain scarce. For smaller particle diameters $( \leq 1 0 0 ~ \mathrm { n m } )$ , densities up to $1 . 1 \times 1 0 ^ { 1 0 } \ : \mathrm { N W / c m ^ { 2 } }$ have been reported using sputterbased deposition, albeit with very small NW radii of 2.8 nm.<sup>51</sup> In comparison, solution-based Au colloid deposition has achieved densities of $1 . 8 { \times } 1 0 ^ { 8 } \ \mathrm { N W / c m ^ { 2 } }$ for Si NWs (50 nm Au colloids),<sup>52</sup> and $7 . 3 { \times } 1 0 ^ { 7 } \ \mathrm { N W / c m ^ { 2 } }$ for InGaAs NWs (30 nm Au colloids).<sup>53</sup>

However, these densities are typically associated with small NW diameters, which limit optical absorption. Scaling such approaches to larger diameters remains challenging due to constraints in particle concentration within solutions, particle agglomeration efects and dificulties in achieving suficiently low pitch-to-diameter ratios. As a result, reaching suficient high NW densities required for eficient optical absorption remains a major challenge in unordered particle-assisted growth, thereby limiting their applicability for scalable optoelectronic devices.<sup>44</sup>

In this work, we systematically investigate the limitations and optimization pathways for achieving high NW densities in unordered III-V NW ensembles grown from commercially available Au colloid solutions. We identify catalyst deposition as the dominant limiting factor governing density scaling across diferent colloid sizes. Furthermore, we show that the observed agglomeration behavior cannot be adequately described by simple analytical models, highlighting the need for more advanced modeling approaches. We demonstrate that a pre-anneal growth step previously developed for patterned Au catalyst arrays <sup>15,54</sup> is transferable to solution-deposited colloids and suppresses their mobility and agglomeration during subsequent high-temperature annealing. This results in a density increase of up to one order of magnitude across a wide range of NW diameters.

## 2 Results and Discussion

To investigate the influence of catalyst deposition on achievable NW densities, we systematically examine how the Au seed particle density evolves with repeated deposition cycles of Au colloid solution. As outlined, catalyst particle deposition is directly linked to the maximum attainable NW density<sup>52</sup> and thus represents a fundamental limiting factor for high-density unordered NW growth. A commercially available Au colloid solution was utilized, along with the deposition and fixation procedure, which is described in detail in the Methods Section, and was applied iteratively for up to ten cycles on multiple independent samples. The resulting catalyst-covered surfaces without further processing are shown in Fig. 1. By scanning electron microscopy (SEM) image analysis it can be confirmed that the density of deposited Au colloids increase with the number of deposition cycles. Concurrently, significant agglomeration is observed, particularly after five and ten cycles (Fig. 1(b, c)). These agglomerates predominantly consist of two to three primary colloids, as illustrated in the inset of Fig. 1 (b) and (c).

Quantitative analysis of the SEM images (Fig. 1(d)) confirms a simultaneous increase in both colloid and particle densities with repeated deposition. To quantify the evolution of particle density, colloids and agglomerates were systematically identified and counted using a custom Python-based image analysis routine. Each SEM image covered an area of approximately $4 2 0 ~ \mathrm { { \textmu m } ^ { 2 } }$ , resulting in a total evaluated area of about $6 0 0 0 { - } 1 2 0 0 0 \ \mathrm { \textmu m } ^ { 2 }$ per deposition cycle across multiple independently prepared samples. However, the extracted data deviate significantly from a linear scaling behavior. As shown in Fig. 1(a-c) and further quantified in Fig. 1 (e), both the average particle diameter and the fraction of agglomerated particles exhibit a pronounced non-linear dependence on the number of deposition cycles. In particular, the agglomeration fraction shows a rapid increase during the initial cycles, followed by a more gradual rise at higher cycle numbers, indicating that particle-particle interactions increasingly dominate the deposition process at higher surface coverage. This behavior ultimately limits the achievable particle density despite repeated deposition cycles.

![](images/338267832a1d26cf02e026d7313bf85017f382476b88b8bb8f9520cf6dbd4227.jpg)

![](images/6f43a401afceeaa9ff804e933007861aee7dad7b6cc5103317c37d2b16eb6bd4.jpg)

![](images/14cc0d106f31a771ff5cbd1a22f1afa781fec7600c74893bdee3640f09f7afa8.jpg)

(d)  
![](images/6271c92ca35c37e1dcfda711921dad6f323c53c549ca1dddf97a785321863cf3.jpg)

![](images/faa0d44030aa0f02adcc682e4384adbb2e67bbf4f9becdfe4f670ef2dd76cdfc.jpg)  
Figure 1: SEM images of Au colloid deposition after (a) 1, (b) 5, and (c) 10 successive deposition cycles using a 100 nm Au colloidal solution. The inset in (b) and (c) highlights a representative agglomerate at higher magnification. (d) Median particle densities of deposited Au colloids (blue) and resulting particles considering agglomeration (red). Error bars indicate the minimum and maximum values obtained from the evaluated dataset. (e) Average particle diameter (blue, left axis) and fraction of agglomerated particles (red, right axis) as a function of deposition cycle number

The observed non-linear evolution of particle density and agglomeration points toward particle formation being governed by at least two competing mechanisms rather than independent deposition alone. The initial rapid increase in agglomeration suggests additional contributions beyond independent deposition, potentially arising from deposition-induced changes in the colloidal system. These may include modifications of substrate surface charging after the initial deposition cycle (e.g., due to HCl addition), temperature-dependent efects, concentration gradients building up inside the solution during waiting times, or increased clustering within the colloidal solution prior to subsequent deposition steps.<sup>55–59</sup> In contrast, the slower increase observed at later stages is more consistent with a process resembling a time dependent stochastic deposition. As shown in Fig. 1 (e), the increase in average particle diameter directly correlates with the fraction of agglomerated particles. Notably, the average number of primary colloids per agglomerate remains nearly constant at approximately 2.4 - 2.6 colloids per agglomerated particle for most deposition cycles, with minor deviations for the first and final cycles. This further strengthens the assumption of a time-dependent stochastic deposition. Such stochastic deposition processes can be described using constant-rate event models, such as the Poisson distribution, which is applied in Supplementary Note 1 to model the observed agglomeration behavior.

While simplified Poisson-based models can provide a rough approximation of general trends and overall limitations, as shown in Supplementary Note 1, more refined and specific models are required to accurately capture detailed behaviors, such as the pronounced initial increase in agglomeration observed experimentally. This deviation highlights the importance of additional interaction mechanisms that are not included in such models. Overall, these results demonstrate that particle-particle interactions in solution, surface efects induced by prior deposition, and process parameters such as potential temperature increase and timing play a critical role in determining the final particle distribution. The experimentally observed behavior therefore cannot be fully captured within the simplified modeling framework considered here, as this would require explicitly accounting for the interplay of particle-particle interactions, deposition-induced surface efects, and process-dependent parameters.

Despite these limitations, the results of this study clearly show that repeated deposition cycles of Au colloid solutions enable a substantial increase in both colloid and seed particle densities by approximately one order of magnitude prior to NW growth. The achievable density is currently limited by agglomeration efects and colloid solution concentration. Similar trends were observed for larger colloid diameters (150 nm and 200 nm) shown in supplementary note 2, indicating the generality of the approach.

As indicated by both the Poisson-based model and the experimental observations in Fig. 1(b)-(d), the deposition of Au colloids from solution results in an inherently unordered and partially inhomogeneous distribution of seed particles. While strict size uniformity is not essential for all applications-particularly for photoabsorbers in photovoltaic (PV) and photoelectrochemical (PEC) systems, where broadband absorption can tolerate some variation in diameter, particle density and spatial distribution remain critical parameters for device performance.

To evaluate the impact of these seed particle characteristics on NW growth, homoepitaxial GaAs NWs were grown on GaAs(111)B substrates using MOVPE via the VLS mechanism. Representative results are shown in Fig. 2. As seen in Fig. 2(a), a high vertical yield of NWs is achieved over large areas. However, significant inhomogeneity in both NW length and diameter is observed (Fig. 2(b)), reflecting the non-uniform seed particle distribution.

A comparison of NW density with the corresponding Au particle density reveals a noticeable reduction during growth. The NW density for the sample shown in Fig. 2 is $3 . 7 4 \times 1 0 ^ { 7 }$ NW/cm<sup>2</sup>, corresponding to values expected for approximately 7-8 deposition cycles in Fig.

![](images/4a987fa541287eff6492aa1db1ac86c2e8d188b9a2f9fc6a961dfd0ac03cfabe.jpg)

![](images/65685abd70a77a372c119602ac9613a1dcbc1b07258eed19a583550f77ec4529.jpg)  
Figure 2: SEM images of GaAs nanowires (NWs) grown after 10 Au colloid deposition cycles. (a) Large-area image showing a high vertical yield of NWs. (b) Higher-magnification image revealing significant inhomogeneity in NW length and diameter. Images were acquired at a 30° tilt angle; the average NW length is approximately 3 µm.

1(d), despite 10 cycles being applied. This indicates an efective density reduction of roughly 20% during the growth process. In addition, the average Au particle diameter at the NW top determined from the evaluation of more than 100 NWs, is approximately 160 nm, and therefore about 20 nm larger than the expected Au particle diameter for 10 deposition cycles based on Fig. 1(e). These significantly larger Au particle at the NW top suggest that further agglomeration occurs during the initial stages of NW growth, leading to both increased Au particle size for the NWs and reduced NW density. This behavior can be explained by the MOVPE growth procedure. Prior to NW growth at $4 0 0 ~ ^ { \circ } \mathrm { C } .$ , a high-temperature annealing step at $6 0 0 ~ ^ { \circ } \mathrm { C }$ is applied for several minutes to form a eutectic alloy between the Au particles and the substrate and to remove surface oxides under an arsenic atmosphere. During this step, the mobility of Au particles is significantly increased, promoting particle coalescence. While this efect is negligible at low particle densities, higher densities increase the probability of particle-particle interactions, leading to additional agglomeration and further degradation of spatial uniformity.

To mitigate these efects, strategies for stabilizing the Au seed particles prior to hightemperature annealing are required. One efective approach is the introduction of a preanneal growth step. <sup>15</sup> In this method, a short MOVPE growth step at lower temperatures $\left( 3 2 0 ~ ^ { \circ } \mathrm { C } \right)$ is performed prior to annealing, enabling partial fixation of the particles. Previous studies have shown that this approach can significantly suppress particle mobility and enable homogeneous NW growth even at high densities. <sup>15,54</sup>

In this work, we adapt this pre-anneal growth strategy to unordered colloid-based deposition. The resulting particle behavior for applying only an annealing step at $6 0 0 ~ ^ { \circ } \mathrm { C }$ for 5 minutes under constant As stabilization (a), a pre-anneal growth step at $3 2 0 ~ ^ { \circ } \mathrm { C }$ for $9 0 ~ \mathrm { s }$ with both As and Ga precursors present (b) and both pre-anneal growth and subsequent annealing step (c) followed by cooling to room temperature is shown in Fig. 3. Building

![](images/9d346e89aec7db993116316e596def0b8bbc4ebad3b729b68d2cce1a9bdb7a42.jpg)

![](images/4696348f99f4409ea045ec51dbe8c049896402e6f7fc2aea98570beb15184a3f.jpg)

![](images/12a247e93f0e301415572d68a16a72937d7b4217dc3ab02d8e1927b9ca8e28e7.jpg)

(d)  
Annealing  
![](images/65d570e48ccf42b3c9daefa19a9f53fca1672475ba33a3d5afbd56882c86567e.jpg)

(e)  
![](images/a4d4c416d76f565609292453d00fca4a033b75a9697b1265ee47b2d89bb30340.jpg)

(f) Preanneal growth + Annealing  
![](images/fe185413ee47b0623e78a653d9281af7be6281fe7f59308258c98ef977d84bd6.jpg)  
Figure 3: SEM images of Au seed particles and corresponding diameter histograms for diferent MOVPE process conditions: after 5 min annealing $( \mathrm { a } , \mathrm { d } )$ ; after a 90 s pre-anneal growth step (b, e); and after a 90 s pre-anneal growth step followed by 5 min annealing (c, f). The pre-anneal growth step leads to a reduced average particle diameter and a narrower diameter distribution, indicating improved particle uniformity for samples with 10 deposition cycles. The black vertical lines in the histograms mark the average particle diameter.

on the previously identified role of particle mobility during high-temperature processing, Fig. 3 illustrates the efect of annealing and pre-anneal growth steps on the Au seed particle distribution. After 5 min of high-temperature annealing $\left( \mathrm { F i g . 3 ( a , d ) } \right)$ , a decrease in particle homogeneity is observed, accompanied by a larger average particle diameter within the range corresponding to the NWs shown in Fig. 2. The resulting particle density of $3 . 6 9 \times 1 0 ^ { 7 } ~ 1 / \mathrm { c m } ^ { 2 }$ closely matches the NW density, confirming that particle coalescence during annealing directly limits the achievable NW density. The introduction of a pre-anneal growth step prior to annealing leads to a distinctly diferent particle distribution. The time, III-V ratio and temperature of this pre-anneal growth step are dependent on the particle volume and process parameters to achieve suficient fixation without lateral growth. For the samples shown in Fig. 3 (b) and (c), this time was set to 90 s, while later optimization of subsequent NW growth showed that 60 s pre-anneal growth time (Fig. 4 (a) and (d)) provides a higher proportion of vertical growth with suficient fixation. As shown in Fig. 3((b), (e)), the diameter histogram exhibits a narrow, near-Gaussian distribution, indicating significantly improved uniformity. The average particle diameter is reduced to 121 nm, which is substantially smaller than both the annealed case and the initial particle distribution (Fig. 1 (e)) for 10 deposition cycles. This reduction can be attributed to partial particle fixation during the low-temperature growth step, which suppresses agglomeration and promotes spatial separation of particles. However, this efect is not fully preserved during the subsequent high-temperature annealing. As shown in Fig. 3(c, f), the average particle diameter increases again to approximately 140 nm, indicating partial re-agglomeration colloids which had been previously separated by pre-anneal growth. Nevertheless, the overall particle size distribution remains significantly more uniform compared to the case without pre-anneal growth. This demonstrates that the pre-anneal growth step efectively mitigates the efects of particle mobility while maintaining a suitable particle size for NW growth.

Combining these findings, the optimized process, consisting of repeated colloid deposition followed by a pre-anneal growth step and subsequent annealing, enables both high particle densities and improved uniformity. To evaluate the generality of this approach, NW growth was performed for three diferent Au colloid sizes (100 nm, 150 nm, and 200 nm), as shown in Fig. 4.

For 100 nm colloids, the NW density increases from $4 . 6 5 { \times } 1 0 ^ { 6 } \ \mathrm { N W / c m ^ { 2 } } \ ( \mathrm { F i g . } 4 ( \mathrm { a } ) )$ to

![](images/6131e363117e5dcfad174676a33cf6ef6482983fa12df080fc2a5ef283c526d9.jpg)

![](images/9fcdaffbf7bc95631561d3a67fcd222c00c587e4f4a88922c6fbf02bbbdafafd.jpg)

![](images/8288e90ef4cf398ff1e43d48c973e860563aa4d75873aa125bd509d242669608.jpg)

![](images/d119fb521fa71742f816c25b76f0c4bdaabdf8c4187b12af11c7887badd50b89.jpg)

![](images/ed3f1d11f16e4c73ec89d43543ba169f7429589d7094361d852cf87d6b61ea22.jpg)

![](images/b9af1a81f72ec8f8eb7d05ad0871e87adf2249f2795b6e9858317d4d519bd8ba.jpg)  
Figure 4: First row shows SEM images of the samples with GaAs NWs grown after 1 deposition cycle $\mathrm { ( a ) - ( c ) }$ , while the second row shows samples with GaAs NW samples grown with 10 deposition cycles (d) and (e) as well as 6 deposition cycles (f). The seed particle diameters of the shown samples are: left column 100 nm (a),(d) with NW length of about 4 µm; middle column 150 nm (b), (e) with NW length of 15 µm and 10 µm respectively and right column 200 nm (c),(f) with NW length of roughly 10 µm and 8 µm. SEM images were taken under a $3 0 ^ { \circ }$ tilt angle.

$4 . 7 9 \times 1 0 ^ { 7 }$ $\mathrm { N W / c m ^ { 2 } }$ (Fig. 4(d)), corresponding to an approximately tenfold enhancement. For 150 nm colloids, a similar increase by a factor of about ten is observed, from $3 . 6 6 \times 1 0 ^ { 6 }$ $\mathrm { N W / c m ^ { 2 } \ ( F i g . ~ 4 ( b ) ) } \ \mathrm { t o } \ 3 . 5 2 \times 1 0 ^ { 7 } \mathrm { { N W / c m ^ { 2 } \ ( F i g . ~ 4 ( e ) ) } }$ . For 200 nm colloids, where agglomeration is more pronounced, the number of deposition cycles was reduced to six. Nevertheless, a sixfold increase in density was achieved, from $2 . 4 6 \times 1 0 ^ { 6 }$ $\mathrm { N W / c m ^ { 2 } }$ (Fig. 4(c)) to $1 . 7 6 \times 1 0 ^ { 7 }$ $\mathrm { N W / c m ^ { 2 } \ ( F i g . \ 4 ( f ) ) }$ ), while maintaining a stable average diameter of approximately 255 nm. It is additionally noted that the density of NWs can locally vary throughout the NW ensemble due to the random distribution of the particle deposition. Across all investigated particle sizes, the introduction of the pre-anneal growth step enables the formation of homogeneous, high-density, and vertically aligned NW ensembles with yields exceeding 90%. These results demonstrate that the primary limitation of unordered NW growth using Au colloids, particle agglomeration, can be efectively mitigated by process engineering. Overall, this study establishes a scalable and lithography-free approach for achieving high-density III-V NW ensembles. By combining controlled colloid deposition with tailored growth pre-treatment, NW densities approaching application-relevant regimes can be realized, providing a viable pathway toward more cost-efective integration of NW-based optoelectronic devices.

## 3 Conclusions

This study systematically investigated the possibilities and limitations of achieving high NW densities in unordered, colloid-based growth systems with a focus on scalable and costefective fabrication. It was demonstrated that repeated deposition of Au colloid solutions enables a near-linear increase in seed particle density. However, this approach is fundamentally limited by particle agglomeration during the particle deposition and the resulting loss of spatial uniformity. The observed agglomeration behavior deviates from simple stochastic expectations and cannot be adequately described by a Poisson-based model, highlighting the need for more advanced computational approaches to capture the underlying particle-particle interactions and process-dependent efects. Furthermore, it was shown that controlling particle mobility is essential for maintaining both high density and uniformity. Adapting the previously established pre-anneal stabilization concept to solution-deposited Au colloids effectively suppresses additional thermally induced agglomeration prior to NW growth. This strategy was successfully applied to Au colloids with diameters of 100 nm, 150 nm, and 200 nm, resulting in density increases of up to one order of magnitude while maintaining high vertical yield and improved size uniformity. Overall, the presented approach provides a scalable, lithography-free pathway toward high-density III-V NW ensembles. By combining controlled colloid deposition with tailored process engineering, this method ofers a promising alternative to conventional ordered array fabrication, enabling low-cost and high-throughput integration of bottom-up grown NWs for optoelectronic and photoelectrochemical applications.

## 4 Methods

## 4.0.1 Substrate Preparation

All samples were prepared on p-doped GaAs(111)B substrates (AXT) with a miscut angle of 0.1° and a Zn doping concentration of $\mathrm { { N _ { A } ( Z n ) = 2 . 4 { \times } 1 0 ^ { 1 9 } \ \mathrm { { c m ^ { - 3 } } } } }$ . Prior to processing, substrates were cleaned by sequential immersion in acetone and isopropanol for 30 s each, followed by drying under a nitrogen flow after each step.

## 4.0.2 Au Colloid Deposition

Au colloid solutions with nominal particle diameters of 100 nm, 150 nm, and 200 nm (Sigma-Aldrich, citrate-bufer) were used. Prior to deposition, the solutions were homogenized by manual agitation followed by 10 min of ultrasonication to minimize pre-existing agglomerates. A single deposition cycle was performed by drop-casting the colloid solution onto the substrate surface using a clean pipette. After a waiting period of approximately 20-40 s, a diluted HCl solution (4% HCl) was applied to modify the surface polarization. <sup>60,61</sup> Following an additional waiting period of several minutes, the sample was dried under nitrogen flow. The ratio between HCl solution and colloid solution was maintained at approximately 1:2. Care was taken to avoid overflow of the liquid from the substrate surface, as this was found to significantly afect particle density and reproducibility. Deposition cycles were repeated up to 10 times depending on the target particle density.

## 4.0.3 MOVPE Growth, Thermal Processing and Characterization

The MOVPE temperature sequence and precursor conditions were based on the process reported by Koch et al., <sup>15</sup> with particle-size-dependent pre-anneal durations and flow rates adapted specifically for the colloid-derived catalyst ensembles investigated here. NW growth and thermal treatments were performed using a MOVPE system (Aixtron AIX 200, horizontal reactor). A pre-anneal growth step was introduced prior to high-temperature annealing, following the approach reported by Koch et al. <sup>15</sup> This step was carried out at $3 2 0 ~ ^ { \circ } \mathrm { C }$ with durations adjusted depending on particle size: 60 s for 100 nm, 180 s for 150 nm, and 300 s for 200 nm colloids. For temperatures above $3 0 0 ~ ^ { \circ } \mathrm { C }$ , a constant arsenic supply was maintained using tertiarybutylarsine (TBAs) with molar flow rates of 49 µmol/min (100 nm and 200 nm samples) and 37 µmol/min (150 nm samples). Trimethylgallium (TMGa) was used as the gallium precursor with a molar flow rate of 19 µmol/min during both the pre-anneal growth step and subsequent NW growth. Annealing was performed at $6 0 0 ~ ^ { \circ } \mathrm { C }$ for 5 min under arsenic overpressure. NW growth was then carried out at $4 3 0 ~ ^ { \circ } \mathrm { C }$ via the VLS mechanism.

Surface morphology and particle distributions were characterized using SEM (Hitachi S-4800) in secondary electron imaging mode. Images were taken at $\textup { a } 3 0 ^ { \circ }$ tilt angle at 10 kV acceleration voltage.

## Supporting Information Available

Further details on the insuficient pure statistical modeling of the Au colloid deposition as a Poisson-like process as well as the general nature of the agglomeration increase for diferent colloid diameters are provided in the Supplementary Material.

## Acknowledgement

The authors gratefully acknowledge the financial support received from the Carl-Zeiss-Stiftung for the “SustEntMat” project (funding code: P2023-02-008). Support by the Center of Micro- and Nanotechnologies (ZMN), a DFG-funded core facility (project number 233759584) of the TU Ilmenau, is gratefully acknowledged. The authors thank W. Prost for valuable discussions and constructive feedback on the manuscript and A. M¨uller for the experimental support. GPT-5.3 (OpenAI) and DeepL Write were used solely for language editing, grammar improvement, and stylistic polishing of author-written text. All scientific content, data interpretation, and conclusions were reviewed and verified by the authors.

## References

(1) Li, D.; Lan, C.; Manikandan, A.; Yip, S.; Zhou, Z.; Liang, X.; Shu, L.; Chueh, Y.-L.; Han, N.; Ho, J. C. Ultra-fast photodetectors based on high-mobility indium gallium antimonide nanowires. Nat. Commun. 2019, 10, 1664.

(2) Shoaib, M. et al. Directional Growth of Ultralong CsPbBr<sub>3</sub> Perovskite Nanowires for High-Performance Photodetectors. J. Am. Chem. Soc. 2017, 139, 15592–15595.

(3) Barrig´on, E.; Heurlin, M.; Bi, Z.; Monemar, B.; Samuelson, L. Synthesis and Applications of III-V Nanowires. Chem. Rev. 2019, 119, 9170–9220.

(4) Krogstrup, P.; Jørgensen, H. I.; Heiss, M.; Demichel, O.; Holm, J. V.; Aagesen, M.;

Nygard, J.; Fontcuberta i Morral, A. Single-nanowire solar cells beyond the Shockley– Queisser limit. Nat. Photonics 2013, 7, 306–310.

(5) Koester, R.; Sager, D.; Quitsch, W.-A.; Pfingsten, O.; Poloczek, A.; Blumenthal, S.; Keller, G.; Prost, W.; Bacher, G.; Tegude, F.-J. High-Speed GaN/GaInN Nanowire Array Light-Emitting Diode on Silicon(111). Nano Lett. 2015, 15, 2318–2323.

(6) Azizar Rahman, M.; Rabiur Rahaman, M.; Pramanik, T.; Ton-That, C. Defect engineering and carrier dynamics in gallium-doped zinc oxide nanowires for light-emitting applications. J. Mater. Chem. C 2025, 13, 5814–5822.

(7) Johar, M. A.; Song, H.-G.; Waseem, A.; Hassan, M. A.; Bagal, I. V.; Cho, Y.-H.; Ryu, S.-W. Universal and scalable route to fabricate GaN nanowire-based LED on amorphous substrate by MOCVD. Appl. Mater. Today 2020, 19, 100541.

(8) Ahn, M.-W.; Park, K.-S.; Heo, J.-H.; Kim, D.-W.; Choi, K. J.; Park, J.-G. On-chip fabrication of ZnO-nanowire gas sensor with high gas sensitivity. Sens. Actuators, B 2009, 138, 168–173.

(9) Akbari-Saatlu, M.; Procek, M.; Mattsson, C.; Thungstr¨om, G.; Nilsson, H.-E.; Xiong, W.; Xu, B.; Li, Y.; Radamson, H. H. Silicon Nanowires for Gas Sensing: A Review. Nanomaterials 2020, 10, 2215.

(10) Cho, I.; Sim, Y. C.; Cho, M.; Cho, Y.-H.; Park, I. Monolithic Micro Light-Emitting Diode/Metal Oxide Nanowire Gas Sensor with Microwatt-Level Power Consumption. ACS Sens. 2020, 5, 563–570.

(11) Koch, J.; Bohlemann, C. Y.; Shekarabi, S.; Ostheimer, D.; Kleinschmidt, P.; Hannappel, T. Exploring the Role of III–V Semiconductor–Based Nanowire Composition and Geometry on Photoelectrochemical Reactions. Adv. Energy Sustainability Res. 2026, 7, e202500156.

(12) Hannappel, T. et al. Integration of Multijunction Absorbers and Catalysts for Eficient Solar–Driven Artificial Leaf Structures: A Physical and Materials Science Perspective. Sol. RRL 2024, 8, 2301047.

(13) Vanka, S.; Arca, E.; Cheng, S.; Sun, K.; Botton, G. A.; Teeter, G.; Mi, Z. High Eficiency Si Photocathode Protected by Multifunctional GaN Nanostructures. Nano Lett. 2018, 18, 6530–6537.

(14) Xu, Y.; Gong, T.; Munday, J. N. The generalized Shockley-Queisser limit for nanostructured solar cells. Sci. Rep. 2015, 5, 13536.

(15) Koch, J.; Qiu, J.; Bohlemann, C. Y.; Ostheimer, D.; Zhao, H.; Kleinschmidt, P.; Lei, Y.; Hannappel, T. Pattern Fidelity of Vertically Aligned GaAs Nanowire Arrays. Small 2025, 21, e06173.

(16) Li, Z.; Allen, J.; Allen, M.; Tan, H. H.; Jagadish, C.; Fu, L. Review on III-V Semiconductor Single Nanowire-Based Room Temperature Infrared Photodetectors. Materials 2020, 13, 1400.

(17) Nagelein, A.; Timm, C.; Steidl, M.; Kleinschmidt, P.; Hannappel, T. Multi-Probe Electrical Characterization of Nanowires for Solar Energy Conversion. IEEE J. Photovolt. 2019, 9, 673–678.

(18) Jeddi, H.; Witzigmann, B.; Adham, K.; Hrachowina, L.; Borgstr¨om, M. T.; Pettersson, H. Spectrally Tunable Broadband Gate-All-Around InAsP/InP Quantum Discsin-Nanowire Array Phototransistors with a High Gain-Bandwidth Product. ACS Photonics 2023, 10, 1748–1755.

(19) Glas, F. Critical dimensions for the plastic relaxation of strained axial heterostructures in free-standing nanowires. Phys. Rev. B 2006, 74, 121302.

(20) Steidl, M.; Koppka, C.; Winterfeld, L.; Peh, K.; Galiana, B.; Supplie, O.; Kleinschmidt, P.; Runge, E.; Hannappel, T. Impact of Rotational Twin Boundaries and Lattice Mismatch on III-V Nanowire Growth. ACS Nano 2017, 11, 8679–8689.

(21) Krogstrup, P.; Jørgensen, H. I.; Johnson, E.; Madsen, M. H.; Sørensen, C. B.; Morral, A. F. i.; Aagesen, M.; Nyg˚ard, J.; Glas, F. Advances in the theory of III–V nanowire growth dynamics. J. Phys. D: Appl. Phys. 2013, 46, 313001.

(22) Wu, D.; Tang, X.; Wang, K.; He, Z.; Li, X. An Eficient and Efective Design of InP Nanowires for Maximal Solar Energy Harvesting. Nanoscale Res. Lett. 2017, 12, 604.

(23) Wu, D.; Tang, X.; Wang, K.; Li, X. An Analytic Approach for Optimal Geometrical Design of GaAs Nanowires for Maximal Light Harvesting in Photovoltaic Cells. Sci. Rep. 2017, 7, 46504.

(24) Hu, Y.; LaPierre, R. R.; Li, M.; Chen, K.; He, J.-J. Optical characteristics of GaAs nanowire solar cells. J. Appl. Phys. 2012, 112, 104311.

(25) Aberg, I.; Vescovi, G.; Asoli, D.; Naseem, U.; Gilboy, J. P.; Sundvall, C.; Dahlgren, A.; Svensson, K. E.; Anttu, N.; Bjork, M. T.; Samuelson, L. A GaAs Nanowire Array Solar Cell With 15.3% Eficiency at 1 Sun. IEEE J. Photovolt. 2016, 6, 185–190.

(26) Guo, H.; Wen, L.; Li, X.; Zhao, Z.; Wang, Y. Analysis of optical absorption in GaAs nanowire arrays. Nanoscale Res. Lett. 2011, 6, 617.

(27) Otnes, G.; Barrig´on, E.; Sundvall, C.; Svensson, K. E.; Heurlin, M.; Siefer, G.; Samuelson, L.; <sup>˚</sup>Aberg, I.; Borgstr¨om, M. T. Understanding InP Nanowire Array Solar Cell Performance by Nanoprobe-Enabled Single Nanowire Measurements. Nano Lett. 2018, 18, 3038–3046.

(28) Treu, J.; Xu, X.; Ott, K.; Saller, K.; Abstreiter, G.; Finley, J. J.; Koblm¨uller, G. Optical

absorption of composition-tunable InGaAs nanowire arrays. Nanotechnology 2019, 30, 495703.

(29) Hobbs, R. G.; Petkov, N.; Holmes, J. D. Semiconductor Nanowire Fabrication by Bottom-Up and Top-Down Paradigms. Chem. Mater. 2012, 24, 1975–1991.

(30) Tintelott, M.; Pachauri, V.; Ingebrandt, S.; Vu, X. T. Process Variability in Top-Down Fabrication of Silicon Nanowire-Based Biosensor Arrays. Sensors 2021, 21, 5153.

(31) Arjmand, T.; Legallais, M.; Nguyen, T. T. T.; Serre, P.; Vallejo-Perez, M.; Morisot, F.; Salem, B.; Ternon, C. Functional Devices from Bottom-Up Silicon Nanowires: A Review. Nanomaterials 2022, 12, 1043.

(32) Liu, G.; Wen, B.; Xie, T.; Castillo, A.; Ha, J.-Y.; Sullivan, N.; Debnath, R.; Davydov, A.; Peckerar, M.; Motayed, A. Top–down fabrication of horizontally-aligned gallium nitride nanowire arrays for sensor development. Microelectron. Eng. 2015, 142, 58–63.

(33) Demontis, V.; Zannier, V.; Sorba, L.; Rossella, F. Surface Nano-Patterning for the Bottom-Up Growth of III-V Semiconductor Nanowire Ordered Arrays. Nanomaterials 2021, 11, 2079.

(34) Ghazali, N.; Ebert, M.; Ditshego, N.; de Planque, M.; Chong, H. Top-down fabrication optimisation of ZnO nanowire-FET by sidewall smoothing. Microelectron. Eng. 2016, 159, 121–126.

(35) Borgstr¨om, M.; Deppert, K.; Samuelson, L.; Seifert, W. Size- and shape-controlled GaAs nano-whiskers grown by MOVPE: a growth study. J. Cryst. Growth 2004, 260, 18–22.

(36) Persson, A. I.; Larsson, M. W.; Stenstr¨om, S.; Ohlsson, B. J.; Samuelson, L.; Wallenberg, L. R. Solid-phase difusion mechanism for GaAs nanowire growth. Nat. Mater. 2004, 3, 677–681.

(37) Dick, K. A.; Deppert, K.; Karlsson, L. S.; Wallenberg, L. R.; Samuelson, L.; Seifert, W. A New Understanding of Au–Assisted Growth of III–V Semiconductor Nanowires. Adv. Funct. Mater. 2005, 15, 1603–1610.

(38) Dick, K. A. A review of nanowire growth promoted by alloys and non-alloying elements with emphasis on Au-assisted III–V nanowires. Prog. Cryst. Growth Charact. Mater. 2008, 54, 138–173.

(39) Wu, Z. H.; Mei, X. Y.; Kim, D.; Blumin, M.; Ruda, H. E. Growth of Au-catalyzed ordered GaAs nanowire arrays by molecular-beam epitaxy. Appl. Phys. Lett. 2002, 81, 5177–5179.

(40) Bauer, B.; Rudolph, A.; Soda, M.; Fontcuberta i Morral, A.; Zweck, J.; Schuh, D.; Reiger, E. Position controlled self-catalyzed growth of GaAs nanowires by molecular beam epitaxy. Nanotechnology 2010, 21, 435601.

(41) Pierret, A.; Hocevar, M.; Diedenhofen, S. L.; Algra, R. E.; Vlieg, E.; Timmering, E. C.; Verschuuren, M. A.; Immink, G. W. G.; Verheijen, M. A.; Bakkers, E. P. A. M. Generic nano-imprint process for fabrication of nanowire arrays. Nanotechnology 2010, 21, 065305.

(42) Munshi, A. M.; Dheeraj, D. L.; Fauske, V. T.; Kim, D. C.; Huh, J.; Reinertsen, J. F.; Ahtapodov, L.; Lee, K. D.; Heidari, B.; van Helvoort, A. T. J.; Fimland, B. O.; Weman, H. Position-controlled uniform GaAs nanowires on silicon using nanoimprint lithography. Nano Lett. 2014, 14, 960–966.

(43) Messing, M. E.; Hillerich, K.; Johansson, J.; Deppert, K.; Dick, K. A. The use of gold for fabrication of nanowire structures. Gold Bull. 2009, 42, 172–181.

(44) Messing, M. E.; Hillerich, K.; Bolinsson, J.; Storm, K.; Johansson, J.; Dick, K. A.; Deppert, K. A comparative study of the efect of gold seed particle preparation method on nanowire growth. Nano Res. 2010, 3, 506–519.

(45) Xu, H.-Y.; Guo, Y.-N.; Sun, W.; Liao, Z.-M.; Burgess, T.; Lu, H.-F.; Gao, Q.; Tan, H. H.; Jagadish, C.; Zou, J. Quantitative study of GaAs nanowires catalyzed by Au film of diferent thicknesses. Nanoscale Res. Lett. 2012, 7, 589.

(46) Sui, M.; Li, M.-Y.; Kim, E.-S.; Lee, J. Fabrication of self-assembled Au droplets by the systematic variation of the deposition amount on various type-B GaAs surfaces. Nanoscale Res. Lett. 2014, 9, 436.

(47) Garcia-Gil, A.; Biswas, S.; Holmes, J. D. A Review of Self-Seeded Germanium Nanowires: Synthesis, Growth Mechanisms and Potential Applications. Nanomaterials 2021, 11, 2002.

(48) Whiticar, A. M.; M˚artensson, E. K.; Nyg˚ard, J.; Dick, K. A.; Bolinsson, J. Annealing of Au, Ag and Au-Ag alloy nanoparticle arrays on GaAs (100) and (111)B. Nanotechnology 2017, 28, 205702.

(49) Chen, Y.; Pistol, M.-E.; Anttu, N. Design for strong absorption in a nanowire array tandem solar cell. Sci. Rep. 2016, 6, 32349.

(50) J¨ager, S. T.; Strehle, S. Design parameters for enhanced photon absorption in vertically aligned silicon nanowire arrays. Nanoscale Res. Lett. 2014, 9, 511.

(51) Puglisi, R. A.; Bongiorno, C.; Caccamo, S.; Fazio, E.; Mannino, G.; Neri, F.; Scalese, S.; Spucches, D.; La Magna, A. Chemical Vapor Deposition Growth of Silicon Nanowires with Diameter Smaller Than 5 nm. ACS Omega 2019, 4, 17967–17971.

(52) Hochbaum, A. I.; Fan, R.; He, R.; Yang, P. Controlled growth of Si nanowire arrays for device integration. Nano Lett. 2005, 5, 457–460.

(53) Kim, Y.; Joyce, H. J.; Gao, Q.; Tan, H. H.; Jagadish, C.; Paladugu, M.; Zou, J.; Suvorova, A. A. Influence of nanowire density on the shape and optical properties of ternary InGaAs nanowires. Nano Lett. 2006, 6, 599–604.

(54) Otnes, G.; Heurlin, M.; Graczyk, M.; Wallentin, J.; Jacobsson, D.; Berg, A.; Maximov, I.; Borgstr¨om, M. T. Strategies to obtain pattern fidelity in nanowire growth from large-area surfaces patterned using nanoimprint lithography. Nano Res. 2016, 9, 2852–2861.

(55) Whitmer, J. K.; Luijten, E. Sedimentation of aggregating colloids. J. Chem. Phys. 2011, 134, 034510.

(56) Roy, S.; Dietrich, S.; Maciolek, A. Solvent coarsening around colloids driven by temperature gradients. Phys. Rev. E 2018, 97, 042603.

(57) Mar´c, M.; Drzewi´nski, A.; Wolak, W. W.; Dudek, M. R. The influence of heating and cooling on agglomeration processes in aqueous metal oxide nanoparticle suspensions. Colloids Surf., A 2026, 742, 140409.

(58) Ferrar, J. A.; Solomon, M. J. Kinetics of colloidal deposition, assembly, and crystallization in steady electric fields. Soft Matter 2015, 11, 3599–3611.

(59) Chu, H. C. W.; Garof, S.; Tilton, R. D.; Khair, A. S. Advective-difusive spreading of difusiophoretic colloids under transient solute gradients. Soft Matter 2020, 16, 238– 246.

(60) Joyce, H. J.; Gao, Q.; Hoe Tan, H.; Jagadish, C.; Kim, Y.; Zou, J.; Smith, L. M.; Jackson, H. E.; Yarrison-Rice, J. M.; Parkinson, P.; Johnston, M. B. III–V semiconductor nanowires for optoelectronic device applications. Prog. Quantum Electron. 2011, 35, 23–75.

(61) Woodruf, J. H.; Ratchford, J. B.; Goldthorpe, I. A.; McIntyre, P. C.; Chidsey, C. E. D. Vertically oriented germanium nanowires grown from gold colloids on silicon substrates and subsequent gold removal. Nano Lett. 2007, 7, 1637–1642.

# Supplementary Material to Controlling catalyst agglomeration in high-density unordered III–V nanowire growth using Au colloid solutions

Chris Yannic Bohlemann,†<sup>,</sup>‡ Pavithira Manoharan,†<sup>,</sup>‡ Helene Reichel,† Kai Daniel

Hanke,† Peter Kleinschmidt,† Thomas Hannappel,† and Juliane Koch∗<sup>,</sup>†<sup>,</sup>‡

Technische Universit¨at Ilmenau, Fundamentals of Energy Materials & Institute for Micro-

and Nanotechnology, Postbox 100 565, D-98693 Ilmenau

Technische Universit¨at Ilmenau, CZS Junior Research Group for substitution and

recycling strategies for solar energy materials, Postbox 100 565,D-98693 Ilmenau

E-mail: j.koch@tu-ilmenau.de

## Supplementary Note 1

To estimate the probability of agglomeration during Au colloid deposition, a simplified twodimensional Poisson point process is considered. In this framework, Au colloids are assumed to attach to the substrate independently in both time and space. Under this assumption, the probability of finding k colloids within a defined critical area can be described by the Poisson probability mass function:

$$
f (k; \lambda) = \frac {\lambda^ {k} \exp (- \lambda)}{k !}\tag{1}
$$

Here, k denotes the number of Au colloids located within a critical interaction area $\mathrm { A _ { c r i t } }$ and λ represents the expected number of colloids within this area. Agglomeration requires at least two colloids, and therefore only cases with k 2 are considered. For simplicity, the critical area is approximated as a circular region with radius $\mathrm { r _ { c r i t } }$ , which is assumed to be equal to or larger than twice the radius of a single Au colloid. The expected value λ can thus be expressed as:

$$
\lambda = \pi r _ {\mathrm{crit}} ^ {2} \rho_ {\mathrm{Au}}\tag{2}
$$

where $\rho _ { A u }$ is the areal density of Au colloids. Substituting Eq. 2 into Eq. 1 yields:

$$
f (k; r _ {\mathrm{crit}}, \rho_ {\mathrm{Au}}) = \frac {(\pi r _ {\mathrm{crit}} ^ {2} \rho_ {\mathrm{Au}}) ^ {k} \exp (- \pi r _ {\mathrm{crit}} ^ {2} \rho_ {\mathrm{Au}})}{k !}\tag{3}
$$

The cumulative probability for agglomeration (i.e., at least two particles within $\mathrm { A _ { c r i t } } )$ is given by:

$$
P (k \geq 2; r _ {\mathrm{crit}}, \rho_ {\mathrm{Au}}) = 1 - \exp (- \pi r _ {\mathrm{crit}} ^ {2} \rho_ {\mathrm{Au}}) \left(1 + \pi r _ {\mathrm{crit}} ^ {2} \rho_ {\mathrm{Au}}\right)\tag{4}
$$

Using Eq. 4, the probability of agglomeration was calculated based on the experimentally determined median Au colloid densities (cf. Fig. 1(d) in the main text) for diferent assumed values of $\mathrm { r _ { c r i t } }$ . The resulting probabilities for selected deposition cycles are summarized in Table 1.

## Model Limitations

A comparison between the calculated probabilities and the experimental data reveals that the Poisson-based model significantly underestimates the observed agglomeration across all investigated critical radii. This discrepancy indicates that the underlying assumptions of the model are not suficient to describe the deposition process.

Here the main limitations of the model are based on the non-uniform particle size distribution. The Au colloids exhibit a finite size distribution, typically close to Gaussian.

Table 1: Calculated agglomeration probabilities for diferent critical radii compared to experimentally observed agglomeration fractions for a 100 nm Au colloid solution.

<table><tr><td>Cycles</td><td>P(100 nm)</td><td>P(200 nm)</td><td>P(400 nm)</td><td>P(800 nm)</td><td>Experiment</td></tr><tr><td>1</td><td>0.0002%</td><td>0.0028%</td><td>0.0438%</td><td>0.6601%</td><td>9.21%</td></tr><tr><td>2</td><td>0.0011%</td><td>0.0184%</td><td>0.2827%</td><td>3.8868%</td><td>16.10%</td></tr><tr><td>3</td><td>0.0014%</td><td>0.0226%</td><td>0.3465%</td><td>4.69%</td><td>24.55%</td></tr><tr><td>4</td><td>0.0044%</td><td>0.0685%</td><td>1.0179%</td><td>12.18%</td><td>23.57%</td></tr><tr><td>5</td><td>0.0071%</td><td>0.1103%</td><td>1.6061%</td><td>17.82%</td><td>22.13%</td></tr><tr><td>6</td><td>0.0102%</td><td>0.1584%</td><td>2.2624%</td><td>23.40%</td><td>26.17%</td></tr><tr><td>7</td><td>0.0112%</td><td>0.1739%</td><td>2.4704%</td><td>25.05%</td><td>19.34%</td></tr><tr><td>8</td><td>0.0140%</td><td>0.2162%</td><td>3.0294%</td><td>29.21%</td><td>27.80%</td></tr><tr><td>9</td><td>0.0173%</td><td>0.2661%</td><td>3.6752%</td><td>33.62%</td><td>29.20%</td></tr><tr><td>10</td><td>0.0253%</td><td>0.3874%</td><td>5.1881%</td><td>42.58%</td><td>29.41%</td></tr></table>

This leads to a distribution of efective interaction radii, which is not captured by a single $\mathrm { r _ { c r i t } }$ . Further the assumption of independent particle arrival in time and space is likely violated. Interactions within the colloidal solution, as well as surface-mediated efects during deposition, can lead to correlated particle placement. In addition, the neglection of particle mobility during the waiting step at room temperature could lead to surface difusion and mobility of particles after deposition, that are not included in the model. These efects could significantly increase the probability of agglomeration. Finally, process-dependent effects such as surface polarization changes, solvent evaporation dynamics, and colloid–colloid interactions in solution are not considered.

The presented Poisson model provides a useful first-order approximation of the expected agglomeration behavior under idealized conditions. However, it fails to quantitatively reproduce the experimentally observed trends, particularly at low deposition cycles where agglomeration is significantly higher than predicted. This indicates that additional mechanismssuch as correlated deposition, particle interactions, and surface difusion play a dominant role. Consequently, more advanced approaches, such as Monte Carlo models or kinetic models incorporating interaction potentials, are required to accurately understand and predict the agglomeration behavior in colloid-based NW growth systems.

## Supplementary Note 2

As shown in Fig. S1 similar efects of agglomerations with increasing number of cycles are observed. Additionally, it is visible that with increasing Au colloids radius the critical radius r<sub>crit</sub> explained in Supplementary Note 1 will also increase due to geometrical reasons therefore leading to the assumption of an increased agglomeration percentage for the same Au particle densities with increasing particle radius.

![](images/8eb6c314cc6012c51a43722ef7dc212e4788202ed74fe2cc73f5d035a4383c61.jpg)  
Figure S1: SEM images of diferent Au colloids with an diameter of 100 nm ((a)-(c)), 150 nm ((d)-(f)), 200 nm ((g)-(i)) and 1 ((a),(d),(g)), 5 ((b),(e),(h)) and 10 ((c),(f),(i)) depostion cycles. The inserts show enlarged agglomerations of multiple Au colloids.

## TOC Graphic

![](images/1842bb84fede388c4933edf8b8ef279ecf8982a2f28ce51a62d253982aa716d9.jpg)  
10 depostion cycles  
pre growth fixation