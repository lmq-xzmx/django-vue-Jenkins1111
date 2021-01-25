<template>

 <div class="echarts">
      <h2>地图绘制成功</h2>
      <!-- 为 ECharts 准备一个具备大小（宽高）的 DOM -->
       <div :style="{height:'600px',width:'100%'}" ref="myEchart"></div>
     </div>

</template>


<script>
  import * as echarts from 'echarts';
  //import '@/assets/js/china.js';
  import '@/assets/js/fujian.js';

  export default {
    name: "echarts",
    props: ["userJson"],
    data() {
      return {
        chart: null
      };
    },
    mounted() {
      this.chinaConfigure();
    },
    beforeDestroy() {
      if (!this.chart) {
        return;
      }
      this.chart.dispose();
      this.chart = null;
    },
    methods: {
      chinaConfigure() {
        console.log(this.userJson)
        let myChart = echarts.init(this.$refs.myEchart); //这里是为了获得容器所在位置    
        window.onresize = myChart.resize;
        myChart.setOption({ // 进行相关配置
          backgroundColor: "#02AFDB",
          tooltip: {}, // 鼠标移到图里面的浮动提示框
          dataRange: {
            show: false,
            min: 0,
            max: 1000,
            text: ['High', 'Low'],
            realtime: true,
            calculable: true,
            color: ['orangered', 'yellow', 'lightskyblue']
          },
          geo: { // 这个是重点配置区
            map: '福建', // 表示哪里的地图地图
            roam: true,
            label: {
                show: true, // 是否显示对应地名
                color: 'rgba(0,0,0,0.4)'
            },
            
            emphasis: {
              itemStyle: {
                borderColor: 'rgba(0, 0, 0, 0.2)',
                areaColor: null,
                shadowOffsetX: 0,
                shadowOffsetY: 0,
                shadowBlur: 20,
                borderWidth: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
            }
          },
          series: [{
              type: 'scatter',
              coordinateSystem: 'geo' // 对应上方配置
            },
            {
              name: '启动次数', // 浮动框的标题
              type: 'map',
              geoIndex: 0,
              data: [{
                "name": "福州市",
                "value": 599
              }, {
                "name": "泉州市",
                "value": 142
              }]
            }
          ]
        })
      }
    }
  }
</script>
