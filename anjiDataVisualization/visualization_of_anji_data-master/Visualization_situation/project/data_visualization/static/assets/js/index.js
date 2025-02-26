// 立即执行函数，防止变量污染 (function() {})();

// 柱状图模块1，景点平均评分
(function () {
  // 从后端传递的数据
  var data = data_dict_json;

  // 提取地名和平均评分，并按评分递增排序
  data.sort((a, b) => a.average_score - b.average_score);
  var places = data.map(item => item.place);
  var scores = data.map(item => item.average_score);

  // 1.实例化对象
  var myChart = echarts.init(document.querySelector(".bar .chart"));

  // 2.指定配置项和数据
  var option = {
    color: ['#2f89cf'],
    // 提示框组件
    tooltip: {
      trigger: 'axis',
      axisPointer: { // 坐标轴指示器，坐标轴触发有效
        type: 'shadow' // 默认为直线，可选为：'line' | 'shadow'
      }
    },
    // 修改图表位置大小
    grid: {
      left: '0%',
      top: '10px',
      right: '0%',
      bottom: '4%',
      containLabel: true
    },
    // x轴相关配置
    xAxis: [{
      type: 'value',
      // 修改刻度标签，相关样式
      axisLabel: {
        color: "rgba(255,255,255,0.6)",
        fontSize: 12
      },
      // x轴样式不显示
      axisLine: {
        lineStyle: {
          color: "rgba(255,255,255,0.6)",
          width: 2
        }
      },
      // x轴分割线的颜色
      splitLine: {
        lineStyle: {
          color: "rgba(255,255,255,0.1)"
        }
      }
    }],
    // y轴相关配置
    yAxis: [{
      type: 'category',
      data: places,
      axisTick: {
        alignWithLabel: true
      },
      // 修改刻度标签，相关样式
      axisLabel: {
        color: "rgba(255,255,255,0.8)",
        fontSize: 10,
        // 不旋转标签
        rotate: 0,
      },
      // y轴样式不显示
      axisLine: {
        show: false
      }
    }],
    // 系列列表配置
    series: [{
      name: '评分',
      type: 'bar',
      barWidth: '35%',
      // 动态数据
      data: scores,
      itemStyle: {
        // 修改柱子圆角
        barBorderRadius: 5
      },

    }]
  };

  // 3.把配置项给实例对象
  myChart.setOption(option);

  // 4.让图表随屏幕自适应
  window.addEventListener('resize', function () {
    myChart.resize();
  })
})();


// 柱状图模块2 景点门票价格
(function () {
  // 实例化对象
  var myChart = echarts.init(document.querySelector(".bar2 .chart"));

  // 声明颜色数组
   var myColor = [
    '#b2182b', '#b2182b', '#d1e5f0',
    '#fd9001', '#fddbc7', '#f4a582',
    '#d6604d', '#b2182b', '#67001f'
  ];

  // 数据格式化为表格所需的形式，并按门票价格排序
  var data = data_dict_json.map(function (item) {
    return { place: item.place, ticket: item.ticket };
  }).sort(function (a, b) {
    return a.ticket - b.ticket;
  });

  // 指定配置项和数据
  var option = {
    grid: {
      top: "10%",
      left: '35%',
      bottom: '10%',
    },
    xAxis: { show: false },
    yAxis: {
      type: 'category',
      inverse: true,
      axisLine: { show: false },
      axisTick: { show: false },
      axisLabel: { color: "#fff" },
      data: data.map(function (item) { return item.place; })
    },
    series: [{
      name: '门票价格',
      type: 'bar',
      barWidth: 20,
      yAxisIndex: 0,
      itemStyle: {
        barBorderRadius: 20,
        color: function (params) {
          return myColor[params.dataIndex % myColor.length];
        }
      },
      label: {
        show: true,
        position: "inside",
        formatter: "{c}元"
      },
      data: data.map(function (item) { return item.ticket; })
    }]
  };

  // 把配置项给实例对象
  myChart.setOption(option);

  // 让图表随屏幕自适应
  window.addEventListener('resize', function () {
    myChart.resize();
  });
})();



// 酒店价格对比图
(function () {
  var myChart = echarts.init(document.querySelector(".line .chart"));

  // 数据来源
  var data = data_dict_json;

  // 构建横坐标数据
  var xAxisData = data.map(function(item) {
    return item.place;
  });

  // 构建两组柱状图数据
  var seriesData = [
    {
      name: '所有酒店均价',
      type: 'bar',
      data: data.map(function(item) {
        return item.all_average_price;
      })
    },
    {
      name: '三公里内酒店均价',
      type: 'bar',
      data: data.map(function(item) {
        return item.three_mile_num_price;
      })
    }
  ];

  var option = {
    tooltip: {
      trigger: 'axis',
      axisPointer: {
        type: 'shadow'
      }
    },
    legend: {
      data: ["所有酒店均价", "三公里内酒店均价"],
       textStyle: {
    color: '#4c9bfd', // 图例文字颜色

  }
    },
      // 修改图表位置大小
    grid: {


      bottom: '0%',
      containLabel: true
    },
    xAxis: [
      {
        type: 'category',
        data: xAxisData,
        axisTick: {
          alignWithLabel: true
        },
 avoidLabelOverlap: true,
         axisLabel: {
           color: "#4c9bfb", // x轴文本颜色

      rotate: 90 // 设置旋转角度
    }
      }
    ],
    yAxis: [
      {
        type: 'value'
      }
    ],
    series: seriesData
  };

  myChart.setOption(option);

  // 让图表随屏幕自适应
  window.addEventListener('resize', function () {
    myChart.resize();
  });
})();






// 经济价值图
(function () {
  var myChart = echarts.init(document.querySelector(".line2 .chart"));

  function calculateEconomicValue(visit_num, ticket, three_mile_num_price) {
    return visit_num * ticket + (visit_num / 3) * three_mile_num_price;
  }

  // 数据来源
  var data = data_dict_json;

  // 构建横坐标数据
  var xAxisData = data.map(function (item) {
    return item.place;
  });

  // 计算经济价值量并构建数据
  var seriesData = [
    {
      name: '经济价值量',
      type: 'bar',
      data: data.map(function (item) {
        return calculateEconomicValue(item.visit_num, item.ticket, item.three_mile_num_price);
      }),
      itemStyle: {
        color: "#0184d5",
        opacity: 0.8
      }
    }
  ];

  var option = {
    tooltip: {
      trigger: 'axis',
      axisPointer: {
        type: 'shadow'
      }
    },
    legend: {
      data: ["经济价值量"],
      textStyle: {
        color: '#4c9bfd' // 图例文字颜色
      }
    },
    grid: {
      bottom: '0%',
        left:'0%',
      containLabel: true
    },
    xAxis: [
      {
        type: 'category',
        data: xAxisData,
        axisTick: {
          alignWithLabel: true
        },
        avoidLabelOverlap: true,
        axisLabel: {
          color: "#4c9bfb", // x轴文本颜色
          rotate: 90 // 设置旋转角度
        }
      }
    ],
    yAxis: [
      {
        type: 'value',
        axisLabel: {
          textStyle: {
            color: "rgba(255,255,255,.6)",
            fontSize: 12
          }
        },
        axisLine: {
          lineStyle: {
            color: "rgba(255,255,255,.2)"
          }
        },
        splitLine: {
          lineStyle: {
            color: "rgba(255,255,255,.1)"
          }
        }
      }
    ],
    series: seriesData
  };

  myChart.setOption(option);

  // 让图表随屏幕自适应
  window.addEventListener('resize', function () {
    myChart.resize();
  });
})();





// 饼形图1 游客数量
(function () {
  // 初始化第一个图表（游客数量）
  var data = data_dict_json;
   data.sort((a, b) => b.visit_num - a.visit_num);
  var visit_num = data.map(item => ({ value: item.visit_num, name: item.place }));
  var myChart1 = echarts.init(document.querySelector(".pie .chart"));

  // 定义第一个图表选项
  var option1 = {
    color: [
    '#67001f', '#b2182b', '#d6604d',
      '#f4a582', '#fddbc7', '#fd9001',
      '#d1e5f0', '#92c5de', '#4393c3'
    ],
    tooltip: {
      trigger: 'item',
      formatter: '{a} <br/>{b}: {c} ({d}%)'
    },
    legend: {
      bottom: 0,
      left: 10,
      itemWidth: 10,
      itemHeight: 10,
      textStyle: {
        color: "rgba(255,255,255,.5)",
        fontSize: "10"
      }
    },
    series: [{
      name: '游客数量',
      type: 'pie',
      center: ["50%", "42%"],
      radius: ['40%', '60%'],
       roseType: 'radius',
      avoidLabelOverlap: true,
       // 图形的文字标签
      label: {
        fontsize: 8,
         fontFamily: 'Arial, sans-serif'
      },
      // 引导线调整
      labelLine: {
        // 连接扇形图线长(斜线)
        length: 15,
        // 连接文字线长(横线)
        length2: 15
      },

      data: visit_num
    }]
  };

  // 设置第一个图表选项
  myChart1.setOption(option1);

  // 窗口调整大小时自适应
  window.addEventListener('resize', function () {
    myChart1.resize();
  });
})();


// 饼形图2  酒店数量
(function () {
  // 初始化第二个图表（酒店数量）
  var data = data_dict_json;
   data.sort((a, b) => a.hotel_num - b.hotel_num);
  var hotel_num = data.map(item => ({ value: item.hotel_num, name: item.place }));
  var myChart2 = echarts.init(document.querySelector(".pie2 .chart"));

  // 定义第二个图表选项
  var option2 = {
    color: [
    '#67001f', '#b2182b', '#d6604d',
    '#f4a582', '#fddbc7', '#fd9001',
    '#d1e5f0', '#92c5de', '#4393c3'
],

    tooltip: {
      trigger: 'item',
      formatter: '{a} <br/>{b}: {c} ({d}%)'
    },
    legend: {
      bottom: 0,
      left: 10,
      itemWidth: 10,
      itemHeight: 10,
      textStyle: {
        color: "rgba(255,255,255,.5)",
        fontSize: "10"
      }
    },
    series: [{
      name: '酒店数量',
      type: 'pie',
      center: ["50%", "42%"],
      radius: ['40%', '60%'],
      avoidLabelOverlap: true,
        // 图形的文字标签
      label: {
        fontsize: 8,
         fontFamily: 'Arial, sans-serif'
      },
      // 引导线调整
      labelLine: {
        // 连接扇形图线长(斜线)
        length: 15,
        // 连接文字线长(横线)
        length2: 15
      },
      data: hotel_num
    }]
  };

  // 设置第二个图表选项
  myChart2.setOption(option2);

  // 窗口调整大小时自适应
  window.addEventListener('resize', function () {
    myChart2.resize();
  });
})();

//安吉县地图
(function() {
    // 初始化图表
    var myChart = echarts.init(document.querySelector(".map .chart"), 'white', {renderer: 'canvas'});

    // 动态加载 JSON 数据
    fetch("../static/assets/anjidata.json")
        .then(response => response.json())
        .then(data => {
            // 注册地图
            echarts.registerMap('anjiDataVisualization', data);

            // 热力图和散点图数据
            var heatmapData = [
                {"name": "中南百草原", "value": [119.662854, 30.678513, 81.5]},
                {"name": "云上草原", "value": [119.661214, 30.452862, 90.84]},
                {"name": "余村两山景区", "value": [119.611085, 30.530665, 68.8]},
                {"name": "安吉竹博园", "value": [119.667327, 30.59742, 74.2]},
                {"name": "藏龙百瀑", "value": [119.617473, 30.44538,58.8]},
                {"name": "江南天池", "value": [119.600502, 30.471173, 57.5]},
                {"name": "灵溪山风景区", "value": [119.646998, 30.477688, 51.37]},
                {"name": "浙北大峡谷", "value": [119.528384, 30.447614, 56.03]},
                {"name": "凤凰山森林公园", "value": [119.713867, 30.623228, 59.33]}
            ];

            // 配置选项
            var option = {
                // 动画相关配置
                animation: true,
                animationThreshold: 2000,
                animationDuration: 1000,
                animationEasing: "cubicOut",
                animationDelay: 0,
                animationDurationUpdate: 300,
                animationEasingUpdate: "cubicOut",
                animationDelayUpdate: 0,

                // 无障碍设置
                aria: {
                    enabled: false
                },

                // 地理坐标系组件
                geo: {
                    map: "anjiDataVisualization",
                    label: {
                        show: false,
                        color: '#ffffff'
                    },
                    roam: true,
                    itemStyle: {
                        normal: {
                            areaColor: 'rgba(34, 70, 168, 0.7)',
                            borderColor: 'rgb(143,132,237)'
                        },
                        emphasis: {
                            areaColor: 'rgba(119, 139, 224, 0.548)'
                        }
                    }
                },

                // 系列列表
                series: [
                    {
                        type: "heatmap",
                        coordinateSystem: "geo",
                        data: heatmapData,
                        pointSize: 20,
                        blurSize: 20,
                        label: {
                            normal: {
                                formatter: '{b}',
                                position: 'right',
                                show: false
                            },
                            emphasis: {
                                show: false
                            }
                        },
                        itemStyle: {
                            emphasis: {
                                color: 'rgba(255,0,0,1)'
                            }
                        },
                        zlevel: 3,
                        z: 4
                    },
                    {
                        type: 'scatter',
                        coordinateSystem: 'geo',
                        data: heatmapData,
                        symbolSize: 8,
                        label: {
                            normal: {
                                formatter: '{b}',
                                position: 'right',
                                color:'rgb(0,149,255)',
                                avoidLabelOverlap: true,
                                show: true

                            },
                            emphasis: {
                                show: true
                            }
                        },
                        itemStyle: {
                            normal: {
                                color: 'rgba(255,127,127,0.62)'
                            },
                            emphasis: {
                                color: 'rgb(214,255,29)'
                            }
                        },
                        zlevel: 3,
                        z: 4
                    },
                    {
                        type: "map",
                        name: "anjiDataVisualization",
                        roam: true,
                        aspectScale: 0.75,
                        nameProperty: "name",
                        selectedMode: false,
                        zoom: 1,
                        zlevel: 0,
                        z: 2,
                        seriesLayoutBy: "column",
                        datasetIndex: 0,
                        mapValueCalculation: "sum",
                        showLegendSymbol: true,
                        itemStyle: {
                            normal: {
                                areaColor: 'rgba(34, 70, 168, 0.7)',
                                borderColor: '#0692a4'
                            },
                            emphasis: {
                                areaColor: 'rgba(119, 139, 224, 0.548)'
                            },
                            borderColor: "rgba(0, 0, 0, 0.5)",
                            borderWidth: 1,
                            areaColor: "rgb(0,110,254)"
                        },
                        emphasis: {
                            itemStyle: {
                                areaColor: 'rgba(119, 139, 224, 0.548)'
                            }
                        }
                    }
                ],

                // 提示框组件
                tooltip: {
                    show: true,
                    trigger: "item",
                    triggerOn: "mousemove|click",
                    axisPointer: {"type": "line"},
                    showContent: true,
                    alwaysShowContent: false,
                    showDelay: 0,
                    hideDelay: 100,
                    enterable: false,
                    confine: false,
                    appendToBody: false,
                    transitionDuration: 0.4,
                    textStyle: {"fontSize": 14},
                    borderWidth: 0,
                    padding: 5,
                    order: "seriesAsc",
                    formatter: function(params) {
                        if (params.seriesType === 'heatmap' || params.seriesType === 'scatter') {
                            return params.name + ': ' + params.value[2];
                        }
                        return params.name;
                    }
                },

                // 标题组件
                title: [
                    {
                        show: true,
                        text: "各大景点分布",
                        target: "blank",
                        subtarget: "blank",
                        padding: 5,
                        itemGap: 10,
                        textAlign: "auto",
                        textVerticalAlign: "auto",
                        triggerEvent: false,
                        textStyle: {
                            color: "#ffffff"
                        }
                    }
                ],

                // 视觉映射组件
                visualMap: {
                    show: true,
                    type: "continuous",
                    min: 0,
                    max: 100,
                    inRange: {
                        color: ['blue', 'green', 'yellow', 'red'],
                        opacity: [0.5, 1]
                    },
                    calculable: true,
                    inverse: false,
                    splitNumber: 5,
                    hoverLink: true,
                    orient: "vertical",
                    padding: 5,
                    showLabel: true,
                    itemWidth: 20,
                    itemHeight: 140,
                    borderWidth: 0,
                    text: ["高", "低"],
                    textGap: 10,
                    precision: 0,
                    textStyle: {
                        color: "#ffffff"
                    },
                    formatter: null
                }
            };

            // 设置选项
            myChart.setOption(option);
        })
        .catch(error => console.error('Error loading the map data:', error));
})();











// 模拟飞行路线地图
// (function () {
//   var myChart = echarts.init(document.querySelector(".map .chart"));
//   var geoCoordMap = {
//     '上海': [121.4648, 31.2891],
//     '东莞': [113.8953, 22.901],
//     '东营': [118.7073, 37.5513],
//     '中山': [113.4229, 22.478],
//     '临汾': [111.4783, 36.1615],
//     '临沂': [118.3118, 35.2936],
//     '丹东': [124.541, 40.4242],
//     '丽水': [119.5642, 28.1854],
//     '乌鲁木齐': [87.9236, 43.5883],
//     '佛山': [112.8955, 23.1097],
//     '保定': [115.0488, 39.0948],
//     '兰州': [103.5901, 36.3043],
//     '包头': [110.3467, 41.4899],
//     '北京': [116.4551, 40.2539],
//     '北海': [109.314, 21.6211],
//     '南京': [118.8062, 31.9208],
//     '南宁': [108.479, 23.1152],
//     '南昌': [116.0046, 28.6633],
//     '南通': [121.1023, 32.1625],
//     '厦门': [118.1689, 24.6478],
//     '台州': [121.1353, 28.6688],
//     '合肥': [117.29, 32.0581],
//     '呼和浩特': [111.4124, 40.4901],
//     '咸阳': [108.4131, 34.8706],
//     '哈尔滨': [127.9688, 45.368],
//     '唐山': [118.4766, 39.6826],
//     '嘉兴': [120.9155, 30.6354],
//     '大同': [113.7854, 39.8035],
//     '大连': [122.2229, 39.4409],
//     '天津': [117.4219, 39.4189],
//     '太原': [112.3352, 37.9413],
//     '威海': [121.9482, 37.1393],
//     '宁波': [121.5967, 29.6466],
//     '宝鸡': [107.1826, 34.3433],
//     '宿迁': [118.5535, 33.7775],
//     '常州': [119.4543, 31.5582],
//     '广州': [113.5107, 23.2196],
//     '廊坊': [116.521, 39.0509],
//     '延安': [109.1052, 36.4252],
//     '张家口': [115.1477, 40.8527],
//     '徐州': [117.5208, 34.3268],
//     '德州': [116.6858, 37.2107],
//     '惠州': [114.6204, 23.1647],
//     '成都': [103.9526, 30.7617],
//     '扬州': [119.4653, 32.8162],
//     '承德': [117.5757, 41.4075],
//     '拉萨': [91.1865, 30.1465],
//     '无锡': [120.3442, 31.5527],
//     '日照': [119.2786, 35.5023],
//     '昆明': [102.9199, 25.4663],
//     '杭州': [119.5313, 29.8773],
//     '枣庄': [117.323, 34.8926],
//     '柳州': [109.3799, 24.9774],
//     '株洲': [113.5327, 27.0319],
//     '武汉': [114.3896, 30.6628],
//     '汕头': [117.1692, 23.3405],
//     '江门': [112.6318, 22.1484],
//     '沈阳': [123.1238, 42.1216],
//     '沧州': [116.8286, 38.2104],
//     '河源': [114.917, 23.9722],
//     '泉州': [118.3228, 25.1147],
//     '泰安': [117.0264, 36.0516],
//     '泰州': [120.0586, 32.5525],
//     '济南': [117.1582, 36.8701],
//     '济宁': [116.8286, 35.3375],
//     '海口': [110.3893, 19.8516],
//     '淄博': [118.0371, 36.6064],
//     '淮安': [118.927, 33.4039],
//     '深圳': [114.5435, 22.5439],
//     '清远': [112.9175, 24.3292],
//     '温州': [120.498, 27.8119],
//     '渭南': [109.7864, 35.0299],
//     '湖州': [119.8608, 30.7782],
//     '湘潭': [112.5439, 27.7075],
//     '滨州': [117.8174, 37.4963],
//     '潍坊': [119.0918, 36.524],
//     '烟台': [120.7397, 37.5128],
//     '玉溪': [101.9312, 23.8898],
//     '珠海': [113.7305, 22.1155],
//     '盐城': [120.2234, 33.5577],
//     '盘锦': [121.9482, 41.0449],
//     '石家庄': [114.4995, 38.1006],
//     '福州': [119.4543, 25.9222],
//     '秦皇岛': [119.2126, 40.0232],
//     '绍兴': [120.564, 29.7565],
//     '聊城': [115.9167, 36.4032],
//     '肇庆': [112.1265, 23.5822],
//     '舟山': [122.2559, 30.2234],
//     '苏州': [120.6519, 31.3989],
//     '莱芜': [117.6526, 36.2714],
//     '菏泽': [115.6201, 35.2057],
//     '营口': [122.4316, 40.4297],
//     '葫芦岛': [120.1575, 40.578],
//     '衡水': [115.8838, 37.7161],
//     '衢州': [118.6853, 28.8666],
//     '西宁': [101.4038, 36.8207],
//     '西安': [109.1162, 34.2004],
//     '贵阳': [106.6992, 26.7682],
//     '连云港': [119.1248, 34.552],
//     '邢台': [114.8071, 37.2821],
//     '邯郸': [114.4775, 36.535],
//     '郑州': [113.4668, 34.6234],
//     '鄂尔多斯': [108.9734, 39.2487],
//     '重庆': [107.7539, 30.1904],
//     '金华': [120.0037, 29.1028],
//     '铜川': [109.0393, 35.1947],
//     '银川': [106.3586, 38.1775],
//     '镇江': [119.4763, 31.9702],
//     '长春': [125.8154, 44.2584],
//     '长沙': [113.0823, 28.2568],
//     '长治': [112.8625, 36.4746],
//     '阳泉': [113.4778, 38.0951],
//     '青岛': [120.4651, 36.3373],
//     '韶关': [113.7964, 24.7028]
//   };
//
//   var XAData = [
//     [{
//       name: '西安'
//     }, {
//       name: '北京',
//       value: 100
//     }],
//     [{
//       name: '西安'
//     }, {
//       name: '上海',
//       value: 100
//     }],
//     [{
//       name: '西安'
//     }, {
//       name: '广州',
//       value: 100
//     }],
//     [{
//       name: '西安'
//     }, {
//       name: '西宁',
//       value: 100
//     }],
//     [{
//       name: '西安'
//     }, {
//       name: '银川',
//       value: 100
//     }]
//   ];
//
//   var XNData = [
//     [{
//       name: '西宁'
//     }, {
//       name: '北京',
//       value: 100
//     }],
//     [{
//       name: '西宁'
//     }, {
//       name: '上海',
//       value: 100
//     }],
//     [{
//       name: '西宁'
//     }, {
//       name: '广州',
//       value: 100
//     }],
//     [{
//       name: '西宁'
//     }, {
//       name: '西安',
//       value: 100
//     }],
//     [{
//       name: '西宁'
//     }, {
//       name: '武汉',
//       value: 100
//     }],
//     [{
//       name: '武汉'
//     }, {
//       name: '西宁',
//       value: 100
//     }],
//     [{
//       name: '武汉'
//     }, {
//       name: '哈尔滨',
//       value: 100
//     }],
//     [{
//       name: '武汉'
//     }, {
//       name: '乌鲁木齐',
//       value: 100
//     }],
//     [{
//       name: '西宁'
//     }, {
//       name: '银川',
//       value: 100
//     }]
//   ];
//
//   var YCData = [
//     [{
//       name: '银川'
//     }, {
//       name: '北京',
//       value: 100
//     }],
//     [{
//       name: '银川'
//     }, {
//       name: '广州',
//       value: 100
//     }],
//     [{
//       name: '银川'
//     }, {
//       name: '上海',
//       value: 100
//     }],
//     [{
//       name: '银川'
//     }, {
//       name: '西安',
//       value: 100
//     }],
//     [{
//       name: '银川'
//     }, {
//       name: '西宁',
//       value: 100
//     }],
//   ];
//
//   var planePath = 'path://M1705.06,1318.313v-89.254l-319.9-221.799l0.073-208.063c0.521-84.662-26.629-121.796-63.961-121.491c-37.332-0.305-64.482,36.829-63.961,121.491l0.073,208.063l-319.9,221.799v89.254l330.343-157.288l12.238,241.308l-134.449,92.931l0.531,42.034l175.125-42.917l175.125,42.917l0.531-42.034l-134.449-92.931l12.238-241.308L1705.06,1318.313z';
//   //var planePath = 'arrow';
//   var convertData = function (data) {
//
//     var res = [];
//     for (var i = 0; i < data.length; i++) {
//
//       var dataItem = data[i];
//
//       var fromCoord = geoCoordMap[dataItem[0].name];
//       var toCoord = geoCoordMap[dataItem[1].name];
//       if (fromCoord && toCoord) {
//         res.push({
//           fromName: dataItem[0].name,
//           toName: dataItem[1].name,
//           coords: [fromCoord, toCoord],
//           value: dataItem[1].value
//         });
//       }
//     }
//     return res;
//
//   };
//
//   var color = ['#a6c84c', '#ffa022', '#46bee9']; //航线的颜色
//   var series = [];
//   [
//     ['西安', XAData],
//     ['西宁', XNData],
//     ['银川', YCData]
//   ].forEach(function (item, i) {
//     series.push({
//       name: item[0] + ' Top3',
//       type: 'lines',
//       zlevel: 1,
//       effect: {
//         show: true,
//         period: 6,
//         trailLength: 0.7,
//         color: 'red', //arrow箭头的颜色
//         symbolSize: 3
//       },
//       lineStyle: {
//         normal: {
//           color: color[i],
//           width: 0,
//           curveness: 0.2
//         }
//       },
//       data: convertData(item[1])
//     }, {
//       name: item[0] + ' Top3',
//       type: 'lines',
//       zlevel: 2,
//       symbol: ['none', 'arrow'],
//       symbolSize: 10,
//       effect: {
//         show: true,
//         period: 6,
//         trailLength: 0,
//         symbol: planePath,
//         symbolSize: 15
//       },
//       lineStyle: {
//         normal: {
//           color: color[i],
//           width: 1,
//           opacity: 0.6,
//           curveness: 0.2
//         }
//       },
//       data: convertData(item[1])
//     }, {
//       name: item[0] + ' Top3',
//       type: 'effectScatter',
//       coordinateSystem: 'geo',
//       zlevel: 2,
//       rippleEffect: {
//         brushType: 'stroke'
//       },
//       label: {
//         normal: {
//           show: true,
//           position: 'right',
//           formatter: '{b}'
//         }
//       },
//       symbolSize: function (val) {
//         return val[2] / 8;
//       },
//       itemStyle: {
//         normal: {
//           color: color[i],
//         },
//         emphasis: {
//           areaColor: '#2B91B7'
//         }
//       },
//       data: item[1].map(function (dataItem) {
//         return {
//           name: dataItem[1].name,
//           value: geoCoordMap[dataItem[1].name].concat([dataItem[1].value])
//         };
//       })
//     });
//   });
//   var option = {
//     tooltip: {
//       trigger: 'item',
//       formatter: function (params, ticket, callback) {
//         if (params.seriesType == "effectScatter") {
//           return "线路：" + params.data.name + "" + params.data.value[2];
//         } else if (params.seriesType == "lines") {
//           return params.data.fromName + ">" + params.data.toName + "<br />" + params.data.value;
//         } else {
//           return params.name;
//         }
//       }
//     },
//     legend: {
//       orient: 'vertical',
//       top: 'bottom',
//       left: 'right',
//       data: ['西安 Top3', '西宁 Top3', '银川 Top3'],
//       textStyle: {
//         color: '#fff'
//       },
//       selectedMode: 'multiple'
//     },
//     geo: {
//       map: 'china',
//       // 把地图放大1.2倍
//       zoom: 1.2,
//       label: {
//         // 鼠标移动显示区域名称
//         emphasis: {
//           show: true,
//           color: '#fff'
//         }
//       },
//       roam: true,
//       // 地图样式修改
//       itemStyle: {
//         normal: {
//           areaColor: 'rgba(34, 70, 168, 0.7)',
//           borderColor: '#0692a4'
//         },
//         emphasis: {
//           areaColor: 'rgba(119, 139, 224, 0.548)'
//         }
//       }
//     },
//     series: series
//   };
//
//   myChart.setOption(option);
//   window.addEventListener('resize', function () {
//     myChart.resize();
//   })
// })();


