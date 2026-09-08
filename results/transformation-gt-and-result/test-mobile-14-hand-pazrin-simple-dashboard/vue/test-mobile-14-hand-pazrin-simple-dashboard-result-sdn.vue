<template>
    <v-container max-width="1024" class="pa-4 ma-0">
		<v-row style="margin-top: 0px">
			<v-col cols="2" offset="0">
<div obj="switch">
      <div class="w-100 px-2">
    <v-switch
      color="primary"
      class="w-100 pl-1"
      density="compact"
      label=""
      hide-details
    ></v-switch>
  </div>

</div>
			</v-col>
			<v-col cols="2" offset="0">
<div obj="checkbox">
      <div class="w-100 px-2">
    <v-checkbox
      class="w-100"
      density="compact"
      label="Checkbox"
      hide-details
    ></v-checkbox>
  </div>

</div>
			</v-col>
			<v-col cols="3" offset="0">
<div obj="key-value">
    <div>
    <v-table
      density="compact"
      class="table"
      style="width: 100%; border-collapse: collapse; table-layout: fixed;">
      
      
      <tbody>
<tr><td>Key</td><td>Value</td></tr>
</tbody>

    </v-table>
  </div>

</div>
			</v-col>
		</v-row>
		<v-row style="margin-top: 0px">
			<v-col cols="4" offset="0">
<div obj="line-chart">
    <div  class="px-1 w-100"></div>
</div>
			</v-col>
			<v-col cols="5" offset="1">
<div obj="switch">
      <div class="w-100 px-2">
    <v-switch
      color="primary"
      class="w-100 pl-1"
      density="compact"
      label=""
      hide-details
    ></v-switch>
  </div>

</div>
			</v-col>
		</v-row>
		<v-row style="margin-top: 0px">
			<v-col cols="11" offset="0">
<div obj="list">
    <div>
    <v-table
      density="compact"
      class="table"
      style="width: 100%; border-collapse: collapse; table-layout: fixed;">
      
      
      <tbody>
<tr><td>List Cell</td></tr>
<tr><td>List Cell</td></tr>
<tr><td>List Cell</td></tr>
<tr><td>List Cell</td></tr>
<tr><td>List Cell</td></tr>
<tr><td>List Cell</td></tr>
</tbody>

    </v-table>
  </div>

</div>
			</v-col>
		</v-row>
		<v-row style="margin-top: 0px">
			<v-col cols="7" offset="2">
<div obj="pie-chart">
    <div  class="px-1 w-100"></div>
</div>
			</v-col>
		</v-row>
		<v-row style="margin-top: 0px">
			<v-col cols="7" offset="2">
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
			<v-col cols="2" offset="1">
<div obj="switch">
      <div class="w-100 px-2">
    <v-switch
      color="primary"
      class="w-100 pl-1"
      density="compact"
      label=""
      hide-details
    ></v-switch>
  </div>

</div>
			</v-col>
			<v-col cols="3" offset="2">
<div obj="label">
    <div class='ui-label' style="width: 100%;">
            <div  style="color: #000; padding-right:0px; padding-left:0px; line-height: 30px; font-weight: 'normal'; background-color: transparent; font-size: 16px; text-align: left; border-radius: 0px">
              Label
            </div>
          </div>

</div>
			</v-col>
			<v-col cols="2" offset="1">
<div obj="switch">
      <div class="w-100 px-2">
    <v-switch
      color="primary"
      class="w-100 pl-1"
      density="compact"
      label=""
      hide-details
    ></v-switch>
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
