<template>
  <v-content>
    <v-container fluid fill-height>
      <v-layout align-center justify-center>
        <v-flex xs12>
          <v-card class="elevation-12">
            <v-toolbar dark color="primary">
              <v-toolbar-title>{{appName}} - Viewer</v-toolbar-title>
            </v-toolbar>
            <v-card-text>
              <p class="subheading">{{wijsheid}}</p>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn @click="refresh">Refresh</v-btn>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </v-content>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { appName } from '@/env';
import { dispatchGetWijsheid } from '@/store/main/actions';

@Component
export default class Login extends Vue {
  public valid = true;
  public username: string = '';
  public appName = appName;
  public wijsheid: string = 'loading wijsheid';

  public refresh() {
    this.wijsheid = 'new wijsheid';
    dispatchGetWijsheid(this.$store);
  }


}
</script>

<style>
</style>
