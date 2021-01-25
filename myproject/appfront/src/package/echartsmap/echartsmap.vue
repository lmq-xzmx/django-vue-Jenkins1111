<template>

 <div class="echarts">
    <div id="main" style="width: 1000px;height:800px;"></div>
    <div class="left_center_map" id="main">
     </div>
     </div>

</template>


<script>
  import * as echarts from 'echarts';
  //import '@/assets/js/china.js'; //请讲区域地图绘制的js文件此处导入
  //import '@/assets/js/fujian.js'; //请讲区域地图绘制的js文件此处导入
  import JSON from '@/assets/json/gulou.json'


  export default {
    name: "echarts",
    //props: ["userJson"],
    data() {
      return {
        chart: null
      };
    },
    mounted () {
        this.leftCenterMap()
      },
    
      methods: {
        leftCenterMap () {
          var myChart = echarts.init(document.getElementById('main')) // 拿到一个实例
          echarts.registerMap('鼓楼区', JSON, {})//引入地图文件
          console.log(JSON)
          var option = {
            backgroundColor: "#02AFDB",//背景：蓝色 ""  
            tooltip: {}, // 鼠标移到图里面的浮动提示框
            title:{
                show:true,
                text: "福州市五区八县地图",
                ubtext: "Sub Title",
                textStyle:{
                fontStyle:"italic"
               }
            },
            geo: { // 这个是重点配置区
              map: '鼓楼区', // 表示哪里的地图地图
              roam: true,
              show: true,//是否显示地理坐标系组件,默认是true
              label: {
                  show: true, // 是否显示对应地名
                  position: 'top',
                  rotate:-45,
                  color: 'rgba(0,0,0,0.4)'
              }
             },
            emphasis: { 
				//信息强调相关配置
              itemStyle: {
                borderColor: 'rgba(0, 0, 0, 0.2)',
                areaColor: null,
                borderType:"dashed",
                shadowOffsetX: 0,
                shadowOffsetY: 0,
                shadowBlur: 50,
                borderWidth: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
            },
            
            series: [{
              type: 'scatter',
              
              coordinateSystem: 'geo' // 对应上方配置
            },
            {
              name: '启动次数', // 浮动框的标题
              //show: false,
              type: 'map',
              geoIndex: 0,
              data: [{
                "name": "温泉街道",
                "value": 599
              }, {
                "name": "水部街道",
                "value": 142
              }]
            }
          ]
          }
          myChart.setOption(option)
        }
      }
  }
</script>
