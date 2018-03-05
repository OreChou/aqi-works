# AQI Inference
论文的相关工作

## 数据
### 已有的数据集（郑宇城市空气提供的数据）
|时间维度|数据|区域|
|:---------------:| -------------:| -------------:|
|2014-5-1 ~ 2015-4-30|空气质量分指数（6种污染物）、气象数据|北京、深圳|
|2013-2-8 ~ 2014-2-8|空气质量分指数（3种）、气象数据|北京、上海|

### 我在收集的数据
- [x] 实时的空气质量数据和气象数据
- [ ] 道路网络数据
- [ ] 交通流量数据
- [x] POI数据
- [ ] 微博签到数据

## 论文
### 重要的论文
《U-Air: When Urban Air Quality Inference Meets Big Data》（2013）

《Spatially Fine-grained Urban Air Quality Estimation Using Ensemble Semi-supervised Learning and Pruning》（2016）

《When Remote Sensing Data meet Ubiquitous Urban Data: Fine-Grained Air Quality Inference》（2016）

## 工作计划

|任务|详细|计划完成时间  |状态|
|:------------- |:------------- |:---------------:| -------------:|
|组织张量数据|根据地图的划分，将数据进行重新组织，从而能够形成张量|2017-1-17||
|抓取POI数据|根据地图的划分，去抓取每个区域里面的POI数据|2017-1-18||
|抓取微博签到数据|根据地图的划分，去抓取每个区域里面的POI数据|2017-1-19||
|获取道路网络数据|使用OpenStreetMap，获取道路网络的数据|2017-1-21||


## 区域划分
### 1 划分的范围（以百度坐标BD09为坐标系）
左上的经纬度（116.09041, 40.133989），右下的经纬度（116.81052, 39.700624）
一共划分了3038个以1KM为边长的矩形网格


### 2 CSV数据格式
|区域ID|区域中心经度|区域中心纬度|左上经度|左上纬度|右下经度|右下纬度|监测站ID|
|:------------- |:------------- |:------------- |:------------- |:------------- |:-------------|:-------------|:---------------:|
|0|0|0|0|0|0|0|0|

### 3 划分的截图
![区域划分](https://github.com/OreChou/AQI-inference/blob/master/image/region.png)

## 道路网络数据
![OpenStreetMap](https://github.com/OreChou/AQI-inference/blob/master/image/road_network.png)

### CSV数据格式
|区域ID|Motorway|Trunk|Link road|Waterway|Other|
|:------------- |:------------- |:------------- |:------------- |:------------- |:-------------|
|0|0|0|0|0|0|

## 微博数据
抓取各区域内POI的签到数据量

### CSV数据格式
|区域ID|签到总数|时间|
|:------------- |:------------- |:------------- |
|0|0||


## POI数据
POI使用百度地图提供的数据，主要的工作是通过其提供的众多接口获取实验所需要的数据。
### 1 POI分类
#### 1.1 百度地图POI分类
![百度地图API分类](https://github.com/OreChou/AQI-inference/blob/master/image/baidu_poi.png)
#### 1.2 论文的POI分类
![郑宇城市空气分类](https://github.com/OreChou/AQI-inference/blob/master/image/poi_uair.png)

![张量分解分类](https://github.com/OreChou/AQI-inference/blob/master/image/poi_tensor.png)
#### 1.3 我的POI分类
一级分类  | 百度地图对应的分类
------------- | -------------
汽车服务（Vehicle Services）  | 汽车服务
交通设施（Transportation spots）| 交通设施
美食（Food）  | 美食
酒店（Hotels and real estates）| 酒店
购物（Shopping）| 购物
教育培训 & 文化传媒（Education & Culture）|教育培训 & 文化传媒
旅游景点|旅游景点
休闲娱乐 & 运动健身|休闲娱乐 & 运动健身
公司企业|公司企业 & 金融 & 房地产
生活服务|生活服务 & 丽人

## 交通流量数据
### 百度地图实时交通图
![张量分解分类](https://github.com/OreChou/AQI-inference/blob/master/image/traffic.png)
通过图像分析的方法，去分析图像中各区域里面不同的拥堵情况

## 实验思路
### 实验一
使用郑宇城市计算的数据集进行实验。额外的数据源：道路网络、POI数据

AQI数据作为张量

上下文矩阵：

区域特征矩阵：道路网络、POI数据特征矩阵

时间特征矩阵：气象特征矩阵

### 实验二
使用自己抓取的数据。

AQI数据作为张量

上下文矩阵：

区域特征矩阵：道路网络、POI数据特征矩阵

时间特征矩阵：交通流量、微博签到、气象特征矩阵

### 实验三
抓取全国空气质量监测站的数据。额外的数据有：交通态势（抓取自高德地图，可描述交通拥堵情况），气象数据（抓取自高德地图、OpenWeatherMap），POI

使用回归模型进行建模