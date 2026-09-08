<template>
    <v-container max-width="1024" class="pa-4 ma-0">
		<v-row style="margin-top: 0px">
			<v-col cols="3" offset="0">
<div obj="label">
    <div class='ui-label' style="width: 100%;">
            <div  style="color: #000; padding-right:0px; padding-left:0px; line-height: 36px; font-weight: 'normal'; background-color: transparent; font-size: 16px; text-align: left; border-radius: 0px">
              Label
            </div>
          </div>

</div>
			</v-col>
		</v-row>
		<v-row style="margin-top: 0px">
			<v-col cols="3" offset="0">
<div obj="input-free-text">
      <div class="w-100 px-2">
    <v-text-field class="w-100" density="compact" label="Input" variant="outlined" bg-color="white" />
  </div>

</div>
			</v-col>
			<v-col cols="3" offset="0">
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
			<v-col cols="3" offset="0">
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
		<v-row style="margin-top: 0px">
			<v-col cols="11" offset="0">
<div obj="line-chart">
    <div  class="px-1 w-100"></div>
</div>
			</v-col>
		</v-row>
		<v-row style="margin-top: 0px">
			<v-col cols="4" offset="0">
<div obj="bar-chart">
    <div  class="px-1 w-100"></div>
</div>
<div obj="pie-chart">
    <div  class="px-1 w-100"></div>
</div>
			</v-col>
			<v-col cols="2" offset="3">
<div obj="image">
      <div style="height: 100%; width: 100%; display: flex; align-items: center; justify-content: center;" >
    <div class="ui-image d-flex justify-center align-center" style="border: 1px #eee solid; width: 100%; height: 100%;">
  <v-icon size="large" icon="mdi-image-area"></v-icon>
  <div>Image</div>
</div>

  </div>

</div>
<div obj="icon-button">
      <div>
    <v-btn
        class="w-100"
        color="primary"
        variant="text"
        
    >
      <div class="align-center">
        <v-icon>mdi-play</v-icon>

        
      </div>
    </v-btn>
  </div>

</div>
			</v-col>
			<v-col cols="2" offset="1">
<div obj="icon-button">
      <div>
    <v-btn
        class="w-100"
        color="primary"
        variant="text"
        
    >
      <div class="align-center">
        <v-icon>mdi-play</v-icon>

        
      </div>
    </v-btn>
  </div>

</div>
<div obj="icon-button">
      <div>
    <v-btn
        class="w-100"
        color="primary"
        variant="text"
        
    >
      <div class="align-center">
        <v-icon>mdi-play</v-icon>

        
      </div>
    </v-btn>
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
