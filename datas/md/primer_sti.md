---
id: primer_sti.md
title: STI 浅槽隔离入门
related_key: STI Shallow Trench Isolation
summary: 浅槽隔离（STI）的作用、基本流程及其与 CMP 的关系。
---

# STI（浅槽隔离）是什么？

**STI**（Shallow Trench Isolation）在硅中刻出浅槽并填入绝缘介质，用于隔离相邻晶体管，防止串扰与漏电路径。它取代了早期不少场景下的 LOCOS 隔离，更适合缩小器件间距。

## 简化流程

1. 垫氧 / 氮化硅硬掩模  
2. 光刻定义隔离区  
3. 刻蚀浅槽  
4. 填充氧化物（常 CVD）  
5. **CMP** 平坦化，去掉多余介质  
6. 去硬掩模，进入后续阱/栅工艺  

## 常见问题（FAQ）

**Q：STI 为什么需要 CMP？**  
A：填充后表面凸起，必须磨平才能做后续光刻与栅形成。

**Q：STI 属于 FEOL 还是 BEOL？**  
A：属于前端（FEOL）隔离，发生在多层金属互连之前。
