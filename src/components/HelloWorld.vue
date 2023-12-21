<template>
  <div>
    <button @click="requestIpAddress">Request IP Address</button>
    <div v-if="ipAddress">Received IP address: {{ ipAddress }}</div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      ipAddress: null,
    };
  },
  methods: {
    requestIpAddress() {
      // Publish an empty message to trigger a response
      this.$mqtt.publish("ip_address_topic", "");
    },
  },
  created() {
    // Subscribe to the MQTT topic when the component is created
    this.$mqtt.subscribe("ip_address_topic", {
      qos: 0, // Quality of Service level (0, 1, or 2)
    });
    
    // Handle incoming messages
    this.$mqtt.on("message", (topic, message) => {
      if (topic === "ip_address_topic") {
        // Update the ipAddress when a message is received
        this.ipAddress = message.toString();
      }
    });
  },
};
</script>
