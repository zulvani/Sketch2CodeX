<template>
    <v-container max-width="1024" class="pa-4 ma-0">
		<v-row style="margin-top: 0px">
			<v-col cols="2" offset="0">
<div obj="list">
    <div>
    <v-table
      density="compact"
      class="table"
      style="width: 100%; border-collapse: collapse; table-layout: fixed;">
      
      
      <tbody>
<tr><td>List Cell</td></tr>
</tbody>

    </v-table>
  </div>

</div>
			</v-col>
			<v-col cols="2" offset="0">
<div obj="common-button">
        <div>
        <v-btn color='primary'>Button</v-btn>
    </div>

</div>
			</v-col>
			<v-col cols="2" offset="0">
<div obj="alert">
      <v-alert>
  <div class="ui-alert">
    Alert
  </div>
  </v-alert>

</div>
			</v-col>
			<v-col cols="2" offset="0">
<div obj="image">
      <div style="height: 100%; width: 100%; display: flex; align-items: center; justify-content: center;" >
    <div class="ui-image d-flex justify-center align-center" style="border: 1px #eee solid; width: 100%; height: 100%;">
  <v-icon size="large" icon="mdi-image-area"></v-icon>
  <div>Image</div>
</div>

  </div>

</div>
			</v-col>
		</v-row>
		<v-row style="margin-top: 0px">
			<v-col cols="5" offset="0">
<div obj="line-chart">
    <div  class="px-1 w-100"></div>
</div>
			</v-col>
			<v-col cols="5" offset="1">
<div obj="bar-chart">
    <div  class="px-1 w-100"></div>
</div>
			</v-col>
		</v-row>
		<v-row style="margin-top: 0px">
			<v-col cols="11" offset="0">
<div obj="hyperlink">
    <div style="margin-top: 2px;">
   <div class="w-100 px-2" style="text-align: left">
      <v-btn
            variant="plain"
            class="w-100 text-start"
            color="primary"
            style="text-transform: none;"
            
        >
          Hyperlink
        </v-btn>
   </div>
</div>

</div>
			</v-col>
		</v-row>
		<v-row style="margin-top: 0px">
			<v-col cols="9" offset="1">
<div obj="pie-chart">
    <div  class="px-1 w-100"></div>
</div>
			</v-col>
		</v-row>
		<v-row style="margin-top: 0px">
			<v-col cols="11" offset="0">
<div obj="slider">
      <div class="w-100 px-2">
    <v-slider
      label=""
    ></v-slider>
  </div>

</div>
			</v-col>
		</v-row>
		<v-row style="margin-top: 0px">
			<v-col cols="1" offset="0">
<div obj="radio-button">
      <div class="w-100 px-2">
    <v-radio
      class="w-100"
      density="compact"
      label="Radio Button"
      hide-details
    ></v-radio>
  </div>

</div>
			</v-col>
			<v-col cols="3" offset="1">
<div obj="label">
    <div class='ui-label' style="width: 100%;">
            <div  style="color: #000; padding-right:0px; padding-left:0px; line-height: 30px; font-weight: 'normal'; background-color: transparent; font-size: 16px; text-align: left; border-radius: 0px">
              Label
            </div>
          </div>

</div>
			</v-col>
			<v-col cols="3" offset="1">
<div obj="label">
    <div class='ui-label' style="width: 100%;">
            <div  style="color: #000; padding-right:0px; padding-left:0px; line-height: 30px; font-weight: 'normal'; background-color: transparent; font-size: 16px; text-align: left; border-radius: 0px">
              Label
            </div>
          </div>

</div>
			</v-col>
			<v-col cols="2" offset="0">
<div obj="input-number">
      <div class="w-100 px-2">
    <v-text-field
      bg-color="white"
      class="w-100"
      density="compact"
      label="0"
      type="number"
      variant="outlined"
    ></v-text-field>
  </div>

</div>
			</v-col>
		</v-row>
    </v-container>
</template>
<script setup lang="ts">
    import {onMounted, onBeforeUnmount, ref} from 'vue'
    import Chart from '@/components/Chart.vue'
    
    onMounted(() => {
    })
    onBeforeUnmount(() => {
    })
</script>
