<template>
    <v-container max-width="1024" class="pa-4 ma-0">
		<v-row style="margin-top: 0px">
			<v-col cols="4" offset="0">
<div obj="label">
    <div class='ui-label' style="width: 100%;">
            <div  style="color: #000; padding-right:0px; padding-left:0px; line-height: 47px; font-weight: 'normal'; background-color: transparent; font-size: 16px; text-align: left; border-radius: 0px">
              Label
            </div>
          </div>

</div>
			</v-col>
		</v-row>
		<v-row style="margin-top: 0px">
			<v-col cols="3" offset="0">
<div obj="date-picker">
      <div class="w-100 px-2">
    <v-menu
      v-model="menu"
      :close-on-content-click="false"
      transition="scale-transition"
      offset-y
      max-width="290px"
      min-width="auto"
    >
      <template #activator="{ props }">
        <v-text-field
          v-bind="props"
          v-model="selectedDate"
          label=""
          append-inner-icon="mdi-calendar"
          readonly
          density="compact"
          hide-details
          variant="outlined"
        ></v-text-field>
      </template>

      <v-date-picker
        v-model="selectedDate"
        @update:model-value="menu = false"
        color="primary"
      ></v-date-picker>
    </v-menu>
  </div>

</div>
			</v-col>
			<v-col cols="3" offset="0">
<div obj="combobox">
      <div class="w-100 px-2">
    <v-combobox
      density="compact"
      label=""
      :items="[]"
      variant="outlined"
    ></v-combobox>
  </div>

</div>
			</v-col>
			<v-col cols="3" offset="0">
<div obj="combobox">
      <div class="w-100 px-2">
    <v-combobox
      density="compact"
      label=""
      :items="[]"
      variant="outlined"
    ></v-combobox>
  </div>

</div>
			</v-col>
		</v-row>
		<v-row style="margin-top: 0px">
			<v-col cols="12" offset="0">
<div obj="undefined">
    <div class='ui-label' style="width: 100%;">
            <div  style="color: #000; padding-right:0px; padding-left:0px; line-height: 232px; font-weight: 'normal'; background-color: transparent; font-size: 16px; text-align: left; border-radius: 0px">
              Label
            </div>
          </div>

</div>
			</v-col>
		</v-row>
		<v-row style="margin-top: 0px">
			<v-col cols="4" offset="0">
<div obj="bar-chart">
    <div  class="px-1 w-100"></div>
</div>
			</v-col>
			<v-col cols="4" offset="0">
<div obj="pie-chart">
    <div  class="px-1 w-100"></div>
</div>
			</v-col>
			<v-col cols="2" offset="0">
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
			<v-col cols="2" offset="0">
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
    const menu = ref(false)
const selectedDate = ref('')

    onMounted(() => {
    })
    onBeforeUnmount(() => {
    })
</script>
