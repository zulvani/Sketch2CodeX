<template>
    <v-container max-width="1024" class="pa-4 ma-0">
		<v-row style="margin-top: 0px">
			<v-col cols="4" offset="0">
<div obj="label">
    <div class='ui-label' style="width: 100%;">
            <div  style="color: #000; padding-right:0px; padding-left:0px; line-height: 38px; font-weight: 'normal'; background-color: transparent; font-size: 16px; text-align: left; border-radius: 0px">
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
			<v-col cols="12" offset="0">
<div obj="common-button">
        <div>
        <v-btn color='primary'>Button</v-btn>
    </div>

</div>
			</v-col>
		</v-row>
		<v-row style="margin-top: 0px">
			<v-col cols="4" offset="0">
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
<div obj="pie-chart">
    <div  class="px-1 w-100"></div>
</div>
			</v-col>
			<v-col cols="2" offset="4">
<div obj="image">
      <div style="height: 100%; width: 100%; display: flex; align-items: center; justify-content: center;" >
    <div class="ui-image d-flex justify-center align-center" style="border: 1px #eee solid; width: 100%; height: 100%;">
  <v-icon size="large" icon="mdi-image-area"></v-icon>
  <div>Image</div>
</div>

  </div>

</div>
<div obj="image">
      <div style="height: 100%; width: 100%; display: flex; align-items: center; justify-content: center;" >
    <div class="ui-image d-flex justify-center align-center" style="border: 1px #eee solid; width: 100%; height: 100%;">
  <v-icon size="large" icon="mdi-image-area"></v-icon>
  <div>Image</div>
</div>

  </div>

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
