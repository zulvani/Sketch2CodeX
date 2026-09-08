<template>
    <v-container max-width="1024" class="pa-4 ma-0">
		<v-row style="margin-top: 0px">
			<v-col cols="11" offset="0">
<div obj="alert">
      <v-alert>
  <div class="ui-alert">
    Alert
  </div>
  </v-alert>

</div>
			</v-col>
		</v-row>
		<v-row style="margin-top: 0px">
			<v-col cols="11" offset="0">
<div obj="key-value">
    <div>
    <v-table
      density="compact"
      class="table"
      style="width: 100%; border-collapse: collapse; table-layout: fixed;">
      
      
      <tbody>
<tr><td>Key</td><td>Value</td></tr>
<tr><td>Key</td><td>Value</td></tr>
<tr><td>Key</td><td>Value</td></tr>
<tr><td>Key</td><td>Value</td></tr>
</tbody>

    </v-table>
  </div>

</div>
			</v-col>
		</v-row>
		<v-row style="margin-top: 0px">
			<v-col cols="3" offset="0">
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
			<v-col cols="5" offset="0">
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
		</v-row>
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
			<v-col cols="8" offset="1">
<div obj="input-free-text">
      <div class="w-100 px-2">
    <v-text-field class="w-100" density="compact" label="Input" variant="outlined" bg-color="white" />
  </div>

</div>
			</v-col>
		</v-row>
		<v-row style="margin-top: 0px">
			<v-col cols="2" offset="0">
<div obj="bar-chart">
    <div  class="px-1 w-100"></div>
</div>
			</v-col>
			<v-col cols="8" offset="1">
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
			<v-col cols="8" offset="1">
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
			<v-col cols="2" offset="0">
<div obj="label">
    <div class='ui-label' style="width: 100%;">
            <div  style="color: #000; padding-right:0px; padding-left:0px; line-height: 30px; font-weight: 'normal'; background-color: transparent; font-size: 16px; text-align: left; border-radius: 0px">
              Label
            </div>
          </div>

</div>
			</v-col>
			<v-col cols="8" offset="1">
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
			<v-col cols="3" offset="2">
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
			<v-col cols="4" offset="1">
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
			<v-col cols="8" offset="2">
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
