<template>
    <v-container max-width="1024" class="pa-4 ma-0">
		<v-row style="margin-top: 0px">
			<v-col cols="4" offset="1">
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
			<v-col cols="10" offset="1">
<div obj="input-free-text">
      <div class="w-100 px-2">
    <v-text-field class="w-100" density="compact" label="Input" variant="outlined" bg-color="white" />
  </div>

</div>
			</v-col>
		</v-row>
		<v-row style="margin-top: 0px">
			<v-col cols="10" offset="1">
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
			<v-col cols="10" offset="1">
<div obj="input-password">
      <div class="w-100 px-2">
    <v-text-field
      bg-color="white"
      class="w-100"
      density="compact"
      label="Password"
      type="password"
      variant="outlined"
    ></v-text-field>
  </div>

</div>
			</v-col>
		</v-row>
		<v-row style="margin-top: 0px">
			<v-col cols="10" offset="1">
<div obj="common-button">
        <div>
        <v-btn color='primary'>Button</v-btn>
    </div>

</div>
			</v-col>
		</v-row>
		<v-row style="margin-top: 0px">
			<v-col cols="6" offset="3">
<div obj="time-picker">
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
		</v-row>
		<v-row style="margin-top: 0px">
			<v-col cols="1" offset="2">
<div obj="image">
      <div style="height: 100%; width: 100%; display: flex; align-items: center; justify-content: center;" >
    <div class="ui-image d-flex justify-center align-center" style="border: 1px #eee solid; width: 100%; height: 100%;">
  <v-icon size="large" icon="mdi-image-area"></v-icon>
  <div>Image</div>
</div>

  </div>

</div>
			</v-col>
			<v-col cols="5" offset="0">
<div obj="slider">
      <div class="w-100 px-2">
    <v-slider
      label=""
    ></v-slider>
  </div>

</div>
			</v-col>
		</v-row>
    </v-container>
</template>
<script setup lang="ts">
    import {onMounted, onBeforeUnmount, ref} from 'vue'
    
    
    onMounted(() => {
    })
    onBeforeUnmount(() => {
    })
</script>
