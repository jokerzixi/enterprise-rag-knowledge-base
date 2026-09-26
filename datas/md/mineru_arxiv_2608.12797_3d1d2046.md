# Vertical $\pmb { \beta } – \mathbf { G a } _ { 2 } \mathbf { O } _ { 3 }$ Isolated Source Electrode Field Effect Transistors (ISEFET) Without Planarization or Mid-Gap Acceptor Blocking Layers

Akilesh Srikanth<sup>1\*</sup>, Md Saklain Morshed<sup>1</sup>, Chandan Joishi<sup>1</sup>, Ahmad E. Islam<sup>3</sup>, and Siddharth Rajan<sup>1,2</sup>

<sup>1</sup>Department of Electrical and Computer Engineering, The Ohio State University, Columbus, OH 43210, USA <sup>2</sup>Department of Material Science and Engineering, The Ohio State University, Columbus, OH 43210, USA <sup>3</sup>Air Force Research Laboratory, Sensors Directorate, Wright-Patterson AFB, Dayton, OH, 45433, USA Corresponding author email: srikanth.24@osu.edu

## Abstract:

We propose and demonstrate the first vertical $\beta { \mathrm { - G a } } _ { 2 } { \mathrm { O } } _ { 3 }$ device architecture without the use of planarization etch back processes or mid-gap acceptor regions. The Isolated Source Electrode Field Effect Transistor (ISEFET) incorporates a dielectric blocking layer to access an isolated source pad extending from the top fin metal. Scaled multi-fin channels were formed by electron beam lithography with a width of 200 nm along with the source pads and then etched to a trench depth of \~1.2 μm. The fabricated devices showed enhancement mode operation with threshold voltage of 2 V and on-off ratio > 10<sup>7</sup> with excellent gate modulation characteristics. The resulting device proved to be comparable to existing vertical transistors and suitable for high-throughput prototyping and large-scale manufacturing of future Gallium oxide and other wide bandgap semiconductor devices.

## Introduction:

Beta-Gallium oxide (β-Ga<sub>2</sub>O<sub>3</sub>) based devices have shown to be potential candidates for future power electronics applications due to their attractive material properties with ultrawide bandgap of $\mathrm { E _ { g } } \sim 4 . 8 \ : \mathrm { e V }$ and theoretical breakdown field up to 8 MV/cm [1-7]. This translates to a superior Baliga Figure of Merit (BFOM) than Si, SiC, and GaN and the availability of high-quality native melt-grown substrates makes it suitable for commercial production with high reliability and lower defects and cost. However, the absence of p-type doping in $\beta { \mathrm { - G a } } _ { 2 } { \mathrm { O } } _ { 3 }$ [8-10] poses significant challenges to efficient device development. Vertical device architectures are preferred for power devices [11-15] compared to lateral counterparts [16-18] due to their high breakdown voltage and high current densities for large-area/current scaling. Successful demonstrations of vertical device topologies in $\beta { \mathrm { - G a } } _ { 2 } { \mathrm { O } } _ { 3 }$ include the Trench MOSFET/FinFET [19-26], U-MOSFET [27-32], and CAVET [33-38]. Vertical FinFETs require multiple dielectric/metal planarization and precision etch processes to successfully produce a working device. U-MOSFET/CAVETs require current blocking layers (CBLs) using mid-gap acceptor regions commonly with N and Mg doping/ion implantation [39] [40] which degrade carrier transport and lead to dispersion and trapping effects. Recent advancements in vertical $\beta { \mathrm { - G a } } _ { 2 } { \mathrm { O } } _ { 3 }$ FinFETs with scaled fin-shaped channels have shown superior device performance with high multi-kilovolt breakdown voltages and low on-resistance [41].

In this work, we report the successful demonstration of the vertical $\beta { \mathrm { - G a } } _ { 2 } { \mathrm { O } } _ { 3 }$ Isolated Source Electrode Field Effect Transistor (ISEFET) made without complex fabrication steps by incorporating a dielectric current blocking layer (CBL) outside the active region of the device to access the source contact. The 3D device schematic for a single-fin ISEFET is shown in Fig 1. (a) and the lateral cross-section along the long dimension of the fin is shown in (b). The source fin metal is buried underneath the gate oxide and gate metal which are conformally deposited over the fins without any planarization etch back involved. This source metal is extended from one side onto a larger bond pad area on top of the CBL region where it can then be accessed. The entire length of the fin metal is defined to be continuous across both the CBL and the $\beta { \mathrm { - G a } } _ { 2 } { \mathrm { O } } _ { 3 }$ surface. There is slight overlap of the gate with the part of the fin having the CBL underneath to ensure all parts of the channel can be electrostatically controlled and prevent any potential leakage paths at the edge of the CBL. This is also beneficial considering there is no need for any critical alignment steps to place the gate immediately at the very edge of the CBL. The source pad region is opened few microns away from the gate edge to prevent shorting of these terminals.

![](images/7f6a5d555693b6cebf35fce954b9f4b16692ca8a3ffa13180908447c2c722193.jpg)

![](images/518ef1f386de591c022261e81f728601cab0f8a56b9ef3cde18c5b418975af20.jpg)  
Fig. 1. (a) Three-dimensional schematic of a single-fin vertical ISEFET and (b) 2-D cross-section showing each layer along the $\mathbf { A } { - } \mathbf { A } ^ { \prime }$ plane

## Device Fabrication:

The ISEFET devices reported here were fabricated on HVPE-grown (001) $\beta { \mathrm { - G a } } _ { 2 } { \mathrm { O } } _ { 3 }$ Sndoped conductive substrates obtained from Novel Crystal Technologies with a drift region thickness of 10 μm and $n ^ { - }$ doping of $1 { \times } 1 0 ^ { 1 6 } \mathrm { c m } ^ { - 3 }$ . The entire device process flow diagram is given in Fig. 2. The top n+ source contact layer with target depth of 150 nm and concentration of $5 \times 1 0 ^ { 1 9 }$ $\mathrm { c m } ^ { - 3 }$ [42] was formed through a multi-energy Si ion implantation. A uniform box plot profile was simulated using the Stopping Range of Ions in Matter (SRIM) software with energies ranging from 15 keV to 170 keV with a total dose of $9 . 1 6 \times 1 0 ^ { 1 4 }$ atoms-cm<sup>-2</sup> as shown in Fig. 3. Post-implant activation annealing was done at 950ºC for 30 mins in ${ \Nu } _ { 2 }$ at a reduced pressure of 360 Torr. Following this, 150 nm of $\mathrm { \dot { S } i O } _ { 2 }$ was deposited using Plasma-Enhanced Chemical Vapor Deposition (PECVD) to serve as the current blocking layer (CBL) of the device. This was formed into separate regions using a combination of Inductively Coupled Plasma Reactive Ion Etching (ICP/RIE) and diluted Buffered HF wet etch. Various fin widths ranging from 0.2 μm-0.4 μm were patterned using Electron Beam Lithography in such a way that a small portion of the fins rested on top of the CBL. Fin metallization was done by electron-beam evaporation of Ti/Au/Ni (40 nm/100 nm/200 nm) to serve as both the source electrode and fin etch mask. An additional metallization step with the same metal stack was done on top of the CBL to form the source pad region. Self-aligned fin etching was done in a $\mathrm { B C l } _ { 3 } / \mathrm { C l } _ { 2 }$ <sub>2</sub>-based ICP/RIE process to achieve a target depth of 1.2 m using the top Ni as the etch mask. The sidewall etch damage was treated in ${ < } 1 0 0 ^ { \mathrm { { o } } } \mathrm { { C } }$ (85%) $\mathrm { H } _ { 3 } \mathrm { P O } _ { 4 }$ for 10 mins. Subsequently, the gate oxide was formed using Plasma-Enhanced Atomic Layer Deposition (PE-ALD) of 40 nm of $\mathrm { A l } _ { 2 } \mathrm { O } _ { 3 }$ . Then, the gate metal was formed by e-beam evaporation and DC sputtering of Ni/Au/Ni (30 nm/70 nm/40 nm) for fin wrapping. Finally, the source pad was opened by removing the $\mathbf { A l } _ { 2 } \mathbf { O } _ { 3 }$ by RIE and drain metallization of Ti/Au (30 nm/100 nm) was done at the backside of the sample. After the source and drain Ohmic contact deposition, a post-metallization anneal (PMA) was performed at $4 7 0 \mathrm { { \% } }$ for 1 min in ${ \Nu } _ { 2 }$ ambient conditions [43].

![](images/1d00774ecf6bd4c3af6fdd247fcc1c6d7e39f80fe146f8961114f4a2ad46f761.jpg)  
Fig. 2. Fabrication process flow for the multi-fin vertical ISEFET

![](images/abb63aa24e2959770d4f6773b9795b39d2d3666bb9dc19fffe741df208246baf.jpg)  
Fig. 3. Simulated SRIM Si implantation profile for n+ contact layer in $\beta { \mathrm { - G a } } _ { 2 } { \mathrm { O } } _ { 3 }$

The completed 0.2 μm multi-fin ISEFET device top-down view is shown in Fig. 4 under optical microscope in (a) along with $8 0 ^ { \mathrm { o } }$ tilted SEM images in (b) and (c). The fins were oriented along the [010] direction with (100)-like sidewalls as these are known to suffer less from the plasma etch damage [44] [45]. All the regions around the device have rounded corners to minimize electric field crowding and prevent pre-mature breakdown.

![](images/c6f6b71e6c2a5d1b32040897add7818522862c5b187c62c12ac915e8e14decc6.jpg)  
Fig. 4. Fully fabricated ISEFET 0.2 μm multi-fin device (a) top-view optical image and $8 0 ^ { \circ }$ tilted SEM image of fins: (b) lateral view and (c) vertical view

## Results and Discussions:

All the testing done on this sample was measured using the Keysight B1505A Semiconductor Device Parameter Analyzer system. The results for this multi-fin device are normalized to an area of $1 0 0 \times 1 0 0 ~ \mu \mathrm { m } ^ { 2 }$ with measured fin width $\mathrm { W } _ { \mathrm { f i n } } { = } 0 . 2 \mu \mathrm { m }$ , interfin spacing $\mathbf { S } _ { \mathrm { f i n } }$ $= 1 . 2 \mu \mathrm { m }$ , fin height $\mathrm { H } _ { \mathrm { f i n } } { = } 1 . 2 ~ \mu \mathrm { m }$ , and fin length ${ \mathrm { L } } _ { \mathrm { f i n } } = 1 0 0 \ { \mu \mathrm { m } }$ . These device dimensions have the highest aspect ratio corresponding to $\mathrm { L _ { g } } { : } \mathsf { W _ { f i n } } = \mathsf { 1 2 } { : } 1$ with double-sided gated sidewalls. The transfer characteristics $\mathrm { ( J _ { D } - V _ { G S } ) }$ for the ISEFET at a positive drain bias $( \mathrm { V } _ { \mathrm { D S } } = 1 \ \mathrm { V } )$ is shown in Fig. 5. (a). The threshold voltage was extracted to be $\mathrm { V } _ { \mathrm { T h } } = 2 \mathrm { ~ V ~ }$ which shows the fins are fully depleted at zero bias and therefore can be operated in E-mode. This device also demonstrates a high $\mathrm { { I _ { o n } } / \mathrm { { I _ { o f f } } \ r a t i o > 1 0 ^ { 7 } } }$ with very low gate leakage (J<sub>G</sub>) observed. There is significant hysteresis observed in these devices after sweeping the gate $\mathrm { ( V _ { G S } ) }$ from depletion bias of -3 V to accumulation at 10 V and back potentially due to the large trap $D _ { \mathrm { i t } }$ at the $\mathrm { A l _ { 2 } O _ { 3 } } / \beta \mathrm { - G a _ { 2 } O _ { 3 } }$ interface from plasma etch damage. This points out that the specific $\mathrm { H } _ { 3 } \mathrm { P O } _ { 4 }$ treatment method used for these devices was insufficient to promote a clean growth surface prior to ALD $\mathbf { A l } _ { 2 } \mathbf { O } _ { 3 }$ deposition. Gate dielectric stacks showing low hysteresis have been demonstrated for Gallium Oxide structures [46-48], and this technology can be adopted for future improvements to the proposed ISEFET.

(a)  
![](images/05ec11b0017e9ccba4be4d4dea756837d3a25c4729c133f6f6827973666b197a.jpg)

(b)  
![](images/15389def931370193b06093b79ba7a404b68b0ed0f87fc4e721f88b1014e5187.jpg)

(c)  
![](images/c16088ec8cb2c96acfe8f74be2ff7d196f3b9cd38e5f833ccb83923af5e99ff5.jpg)

(d)  
![](images/68f349218920be8b5fcd9205e4e9ceb8c58ff78795f2a43505864c150c88e29b.jpg)  
Fig. 5. (a) DC transfer, (b) output, and (c) off-state breakdown characteristics of the fabricated $\beta -$ $\mathrm { G a } _ { 2 } \mathrm { O } _ { 3 }$ ISEFET. (d) Optical micrograph of the device showing destructive breakdown at fin edge

The DC output characteristics $\left( \mathrm { J _ { D } } \mathrm { - V _ { D S } } \right)$ for the ISEFET with the same dimensions as earlier is shown in Fig. 5. (b). The device has excellent gate modulation with an extracted on-resistance $\mathrm { R } _ { \mathrm { o n - s p } } = 6 7 6 \mathrm { m } \Omega \mathrm { - c m } ^ { 2 }$ at an applied gate bias $\mathrm { V } _ { \mathrm { G S } } = 1 5 \mathrm { V } .$ This relatively high resistance was later attributed to the impartial activation/degradation of the Si-implanted $^ { \mathrm { n + } }$ contact layer for this particular sample. Due to this, the highest attained output current density for this device was 12 $\mathrm { A } / \mathrm { c m } ^ { 2 }$ at drain bias $\mathrm { V } _ { \mathrm { D S } } { = } 1 0 \mathrm { V }$ and $\mathrm { V } _ { \mathrm { G S } } = 1 5 \mathrm { V } .$ Additionally, relatively lower aspect ratio structures $\mathrm { L _ { g } } { : } \mathrm { W _ { f i n } } = 6 { : } 1$ with $\mathrm { W } _ { \mathrm { f i n } } = 0 . 4$ μm was also characterized (not shown here). These devices had a maximum output current density of $7 0 \mathrm { A } / \mathrm { c m } ^ { 2 }$ at $\mathrm { V } _ { \mathrm { D S } } = 1 0 \mathrm { V }$ and $\mathrm { V } _ { \mathrm { G S } } = 1 5 \mathrm { V } ,$ I<sub>on</sub>/I<sub>off</sub> ratio $> 1 0 ^ { 9 }$ at $\mathrm { V _ { D S } } = 1 0 \mathrm { V } ,$ and $\mathrm { R } _ { \mathrm { o n - s p } } = 3 2 2 \mathrm { m } \Omega \mathrm { - c m } ^ { 2 }$ which is $2 \mathbf { x }$ lower than the previous device with $\mathrm { W } _ { \mathrm { f i n } } = 0 . 2$ μm. However, it showed triode-like output characteristics with no saturation regime at high drain bias.

Fig. 5. (c) shows the off-state breakdown characteristics for the multi-fin $( \mathrm { W } _ { \mathrm { f i n } } = 0 . 2 \ \mu \mathrm { m } )$ ISEFET at $\mathrm { V } _ { \mathrm { G S } } = { \bf \nabla } - 5 \mathrm { ~ V } .$ The observed breakdown voltage was around $\mathrm { V _ { D S } } = 5 1 0 \mathrm { ~ V ~ }$ while maintaining a low leakage current $( \mathrm { J _ { G } } \sim 1 0 ^ { - 7 } \mathrm { A } / \mathrm { c m } ^ { 2 } )$ at the noise floor of the system throughout the measurement until the breakdown point. This corresponds to a non-punch through breakdown with an electric field of $\mathrm { E } _ { \mathrm { c } } = 1 . 3 4$ MV/cm in the $\beta { \mathrm { - G a } } _ { 2 } { \mathrm { O } } _ { 3 }$ drift region. The physical location of the breakdown was seen at the gate edge of the device periphery close to the source pad region as shown in the optical micrograph in Fig. 5. (d). Prior measurements of the dielectric strength of this specific process of $\mathbf { \Delta A L D A l } _ { 2 } \mathbf { O } _ { 3 }$ have indicated similar breakdown values so the $\mathrm { V } _ { \mathrm { B R } }$ of the transistor is most likely limited by the gate oxide at the MOS interface. Effective field management strategies and oxide spacers at the trench bottom are potential future design criteria for the next generation of $\mathbf { \beta } _ { \beta - \mathbf { G a } _ { 2 } \mathbf { O } _ { 3 } }$ ISEFET devices to further improve the $\mathrm { V } _ { \mathrm { B R } }$

## Conclusion:

In summary, this work shows the fabrication process and results for the first generation of vertical $\beta { \mathrm { - G a } } _ { 2 } { \mathrm { O } } _ { 3 }$ ISEFET achieved without planarization etch back steps or mid-gap acceptor CBL regions by incorporating an isolated source electrode to serve as a large area source contact to the fin metal. This device design allows for rapid prototyping and high yield innovative ideas that could be incorporated into future iterations of the ISEFET without being limited by the nature of the manufacturing process. Initial results for a 0.2 μm multi-fin device showed $\mathrm { V } _ { \mathrm { T h } } { = } 2 \ \mathrm { V } , \ \mathrm { I } _ { \mathrm { o n } } / \mathrm { I } _ { \mathrm { o f f } }$ $> 1 0 ^ { 7 } , \mathrm { R } _ { \mathrm { o n - s p } } = 6 7 6 \mathrm { ~ m } \Omega \mathrm { - c m } ^ { 2 } .$ , and $\mathrm { V } _ { \mathrm { B R } } = 5 1 0 \mathrm { V } .$ This device exhibits transistor characteristics that are not inherently limited by the device architecture itself and rather requires optimization of specific process steps for further improvements. This provides a promising path for development of highly manufacturable vertical $\beta { \mathrm { - G a } } _ { 2 } { \mathrm { O } } _ { 3 }$ high-voltage transistors for power electronics applications.

## Acknowledgements:

A major portion of this work was performed in Nanotech West Cleanroom facility and Characterization Lab. We acknowledge the funding support from the Defense Associated Graduate Student Innovators (DAGSI) Fellowship.

## References:

[1] Pearton, S.J., Yang, J., Cary IV, P.H., Ren, F., Kim, J., Tadjer, M.J. and Mastro, M.A., 2018. A review of Ga2O3 materials, processing, and devices. Applied Physics Reviews, 5(1), p.011301.

[2] Higashiwaki, M. and Jessen, G.H., 2018. Guest Editorial: The dawn of gallium oxide microelectronics. Applied Physics Letters, 112(6).

[3] Sasaki, K., 2024. Prospects for β-Ga2O3: now and into the future. Applied Physics Express, 17(9), p.090101.

[4] Pearton, S.J., Ren, F., Tadjer, M. and Kim, J., 2018. Perspective: Ga2O3 for ultra-high power rectifiers and MOSFETS. Journal of Applied Physics, 124(22).

[5] Higashiwaki, M., Sasaki, K., Kuramata, A., Masui, T. and Yamakoshi, S., 2012. Gallium oxide (Ga2O3) metal-semiconductor field-effect transistors on single-crystal β-Ga2O3 (010) substrates. Applied Physics Letters, 100(1).

[6] Higashiwaki, M., Sasaki, K., Kamimura, T., Hoi Wong, M., Krishnamurthy, D., Kuramata, A., Masui, T. and Yamakoshi, S., 2013. Depletion-mode Ga2O3 metal-oxide-semiconductor fieldeffect transistors on β-Ga2O3 (010) substrates and temperature dependence of their device characteristics. Applied Physics Letters, 103(12).

[7] Green, A.J., Chabak, K.D., Heller, E.R., Fitch, R.C., Baldini, M., Fiedler, A., Irmscher, K., Wagner, G., Galazka, Z., Tetlak, S.E. and Crespo, A., 2016. 3.8-MV/cm Breakdown Strength of MOVPE-Grown Sn-Doped β-Ga2O3 MOSFETs. IEEE Electron Device Letters, 37(7), pp.902- 905.

[8] Peelaers, H., Lyons, J.L., Varley, J.B. and Van de Walle, C.G., 2019. Deep acceptors and their diffusion in Ga2O3. APL Materials, 7(2).

[9] Kyrtsos, A., Matsubara, M. and Bellotti, E., 2018. On the feasibility of p-type Ga2O3. Applied Physics Letters, 112(3).

[10] Varley, J.B., Janotti, A., Franchini, C. and Van de Walle, C.G., 2012. Role of self-trapping in luminescence and p-type conductivity of wide-band-gap oxides. Physical Review B—Condensed Matter and Materials Physics, 85(8), p.081109.

[11] Zhang, Y. and Palacios, T., 2020. (Ultra) wide-bandgap vertical power FinFETs. IEEE Transactions on Electron Devices, 67(10), pp.3960-3971.

[12] Green, A.J., Speck, J., Xing, G., Moens, P., Allerstam, F., Gumaelius, K., Neyer, T., Arias-Purdue, A., Mehrotra, V., Kuramata, A. and Sasaki, K., 2022. β-Gallium oxide power electronics. Apl Materials, 10(2).

[13] Higashiwaki, M., Sasaki, K., Murakami, H., Kumagai, Y., Koukitu, A., Kuramata, A., Masui, T. and Yamakoshi, S., 2016. Recent progress in Ga2O3 power devices. Semiconductor Science and Technology, 31(3), p.034001.

[14] Wong, M.H. and Higashiwaki, M., 2020. Vertical β-Ga₂O₃ power transistors: A review. IEEE Transactions on Electron Devices, 67(10), pp.3925-3937.

[15] Zhou, J., Zhou, X., Liu, Q., Wong, M.H., Xu, G., Yang, S. and Long, S., 2023. Vertical β- Ga2O3 power transistors: Fundamentals, designs, and opportunities. IEEE Transactions on Electron Devices, 71(3), pp.1513-1522.

[16] Wong, M.H., Sasaki, K., Kuramata, A., Yamakoshi, S. and Higashiwaki, M., 2015. Fieldplated Ga2O3 MOSFETs with a breakdown voltage of over 750 V. IEEE Electron Device Letters, 37(2), pp.212-215.

[17] Chabak, K.D., Leedy, K.D., Green, A.J., Mou, S., Neal, A.T., Asel, T., Heller, E.R., Hendricks, N.S., Liddy, K., Crespo, A. and Miller, N.C., 2020. Lateral β-Ga2O3 field effect transistors. Semiconductor Science and Technology, 35(1), p.013002.

[18] Lv, Y., Liu, H., Zhou, X., Wang, Y., Song, X., Cai, Y., Yan, Q., Wang, C., Liang, S., Zhang, J. and Feng, Z., 2020. Lateral β-Ga2O3 MOSFETs with high power figure of merit of 277 MW/cm 2. IEEE Electron Device Letters, 41(4), pp.537-540.

[19] Sasaki, K., Thieu, Q.T., Wakimoto, D., Koishikawa, Y., Kuramata, A. and Yamakoshi, S., 2017. Depletion-mode vertical Ga2O3 trench MOSFETs fabricated using Ga2O3 homoepitaxial films grown by halide vapor phase epitaxy. Applied Physics Express, 10(12), p.124201.

[20] Hu, Z., Nomoto, K., Li, W., Tanen, N., Sasaki, K., Kuramata, A., Nakamura, T., Jena, D. and Xing, H.G., 2018. Enhancement-mode Ga2O3 vertical transistors with breakdown voltage> 1 kV. IEEE Electron Device Letters, 39(6), pp.869-872.

[21] Hu, Z., Nomoto, K., Li, W., Jinno, R., Nakamura, T., Jena, D. and Xing, H., 2019, May. 1.6 kV vertical Ga2O3 FinFETs with source-connected field plates and normally-off operation. In 2019 31st International Symposium on Power Semiconductor Devices and ICs (ISPSD) (pp. 483- 486). IEEE.

[22] Li, W., Nomoto, K., Hu, Z., Nakamura, T., Jena, D. and Xing, H.G., 2019, December. Single and multi-fin normally-off Ga2O3 vertical transistors with a breakdown voltage over 2.6 kV. In 2019 IEEE International Electron Devices Meeting (IEDM) (pp. 12-4). IEEE.

[23] Hu, Z., Nomoto, K., Li, W., Zhang, L.J., Shin, J.H., Tanen, N., Nakamura, T., Jena, D. and Xing, H.G., 2017, June. Vertical fin Ga2O3 power field-effect transistors with on/off ratio> 10 9. In 2017 75th Annual Device Research Conference (DRC) (pp. 1-2). IEEE.

[24] Tetzner, K., Klupsch, M., Popp, A., Bin Anooz, S., Chou, T.S., Galazka, Z., Ickert, K., Matalla, M., Unger, R.S., Treidel, E.B. and Wolf, M., 2023. Enhancement-mode vertical (100) β-Ga2O3 FinFETs with an average breakdown strength of 2.7 MV cm− 1. Japanese Journal of Applied Physics, 62(SF), p.SF1010.

[25] Roy, S., Saha, C.N., Peterson, C., Mitchell, W.J., Speck, J.S. and Krishnamoorthy, S., 2025. Multi-fin β-Ga2O3 Vertical FinFET with Interfin Field Oxide Exhibiting a Breakdown Voltage of 1.8 kV and Power Figure of Merit of 1GW/cm 2. IEEE Electron Device Letters.

[26] Wang, Z., Inajima, J., Tsujimoto, K., Teramura, Y., Iba, Y., Terauchi, Y., Yoshinaga, J., Kamimura, T., Kumagai, Y. and Higashiwaki, M., 2026. Effects of nitrogen radical irradiation on device characteristics of vertical β-Ga2O3 (010) FinFETs. APL Electronic Devices, 2(2).

[27] Liu, Q., Zhou, X., Wong, M.H., Yao, H., Zhou, J., Zhang, X., Xu, G. and Long, S., 2024, June. 1-kV β-Ga2O3 UMOSFET with quasi-inversion nitrogen-ion-implanted channel. In 2024 36th International Symposium on Power Semiconductor Devices and ICs (ISPSD) (pp. 236-239). IEEE.

[28] Zou, Z., Zhang, X., Zeng, C., Chen, T., Guo, G., Li, B., Li, Z., Ma, Y., Zhou, X., Xu, G. and Long, S., 2025. Over 1.3-kV β-Ga₂O₃ Vertical UMOSFET With High Concentration of N-Ion Implantation and Activation Annealing Temperature. IEEE Transactions on Electron Devices, 72(5), pp.2461-2466.

[29] Ma, Y., Zhou, X., Tang, W., Zhang, X., Xu, G., Zhang, L., Chen, T., Dai, S., Bian, C., Li, B. and Zeng, Z., 2023. 702.3 A· cm⁻ ²/10.4 mΩ· cm² β-Ga₂O₃ U-Shape trench gate MOSFET with Nion implantation. IEEE Electron Device Letters, 44(3), pp.384-387.

[30] Liu, Q., Zhou, J., Zhou, X., Wong, M.H., Yao, H., Liu, J., Zhang, X., Xu, G. and Long, S., 2025. Improved blocking capability of N-ion-implanted β-Ga2O3 U-shaped trench gate MOSFET by annealing in oxygen. Applied Physics Express, 18(4), p.041003.

[31] Saha, S., Amir, W., Liu, J., Meng, L., Yu, D., Zhao, H. and Singisetti, U., 2025. E-mode vertical β-Ga2O3 (010) U-trench MOSFETs with in-situ mg-doped current blocking layers. IEEE Electron Device Letters, 46(5), pp.725-728.

[32] Zhou, X., Ma, Y., Xu, G., Liu, Q., Liu, J., He, Q., Zhao, X. and Long, S., 2022. Enhancementmode β-Ga2O3 U-shaped gate trench vertical MOSFET realized by oxygen annealing. Applied Physics Letters, 121(22).

[33] Wong, M.H., Goto, K., Murakami, H., Kumagai, Y. and Higashiwaki, M., 2018. Current Aperture Vertical β-Ga2O3 MOSFETs Fabricated by N-and Si-Ion Implantation Doping. IEEE Electron Device Letters, 40(3), pp.431-434.

[34] Wong, M.H., Murakami, H., Kumagai, Y. and Higashiwaki, M., 2019. Enhancement-Mode β- Ga2O3 Current Aperture Vertical MOSFETs With N-Ion-Implanted Blocker. IEEE Electron Device Letters, 41(2), pp.296-299.

[35] Wong, M.H., Goto, K., Morikawa, Y., Kuramata, A., Yamakoshi, S., Murakami, H., Kumagai, Y. and Higashiwaki, M., 2018. All-ion-implanted planar-gate current aperture vertical Ga2O3 MOSFETs with Mg-doped blocking layer. Applied Physics Express, 11(6), p.064102.

[36] Wong, M.H., Murakami, H., Kumagai, Y. and Higashiwaki, M., 2021. Aperture-limited conduction and its possible mechanism in ion-implanted current aperture vertical β-Ga2O3 MOSFETs. Applied Physics Letters, 118(1).

[37] Chen, X., Li, F. and Hess, H., 2024. Design of Enhancement Mode β-Ga₂O₃ Vertical Current Aperture MOSFETs With a Trench Gate. IEEE access, 12, pp.42791-42801.

[38] Zeng, K., Soman, R., Bian, Z., Jeong, S. and Chowdhury, S., 2022. Vertical Ga2O3 MOSFET with magnesium diffused current blocking layer. IEEE Electron Device Letters, 43(9), pp.1527- 1530.

[39] Zeng, K., 2025. Perspective on vertical Ga₂O₃ power MOSFETs utilizing current blocking layer technology.

[40] Wong, M.H., Lin, C.H., Kuramata, A., Yamakoshi, S., Murakami, H., Kumagai, Y. and Higashiwaki, M., 2018. Acceptor doping of β-Ga2O3 by Mg and N ion implantations. Applied Physics Letters, 113(10).

[41] Wakimoto, D., Lin, C.H., Ema, K., Ueda, Y., Miyamoto, H., Sasaki, K. and Kuramata, A., 2025. A multi-fin normally-off β-Ga2O3 vertical transistor with a breakdown voltage exceeding 10 kV. Applied Physics Express, 18(10), p.106502.

[42] Sasaki, K., Higashiwaki, M., Kuramata, A., Masui, T. and Yamakoshi, S., 2013. Si-ion implantation doping in β-Ga2O3 and its application to fabrication of low-resistance ohmic contacts. Applied Physics Express, 6(8), p.086502.

[43] Tadjer, M.J., 2019. Ohmic contacts to gallium oxide. In Gallium oxide (pp. 211-230). Elsevier.

[44] Li, W., Nomoto, K., Hu, Z., Jena, D. and Xing, H.G., 2019. Fin-channel orientation dependence of forward conduction in kV-class Ga2O3 trench Schottky barrier diodes. Applied Physics Express, 12(6), p.061007.

[45] Dhara, S., Kalarickal, N.K., Dheenan, A., Joishi, C. and Rajan, S., 2022. β-Ga2O3 Schottky barrier diodes with 4.1 MV/cm field strength by deep plasma etching field-termination. Applied Physics Letters, 121(20).

[46] Islam, A.E., Zhang, C., DeLello, K., Muller, D.A., Leedy, K.D., Ganguli, S., Moser, N.A., Kahler, R., Williams, J.C., Dryden, D.M. and Tetlak, S., 2022. Defect engineering at the Al2O3/(010) β-Ga2O3 interface via surface treatments and forming gas post-deposition anneals. IEEE Transactions on Electron Devices, 69(10), pp.5656-5663.

[47] Dhara, S., Dheenan, A., Kalarickal, N.K., Huang, H.L., Islam, A.E., Joishi, C., Fiedler, A., McGlone, J.F., Ringel, S.A., Hwang, J. and Rajan, S., 2023. Plasma-assisted deposition and characterization of Al2O3 dielectric layers on (001) β-Ga2O3. Applied Physics Letters, 123(8).

[48] Islam, A.E., Leedy, K.D., Wang, W., Miesle, A., Liddy, K.J., Dryden, D.M., Hendricks, N.S., Asel, T., Chabak, K.D. and Green, A.J., 2026. Dielectric integration and interface defect engineering in β-Ga2O3 metal–oxide–semiconductor (MOS) devices. APL Electronic Devices, 2(1).