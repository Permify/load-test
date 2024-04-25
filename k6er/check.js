import http from "k6/http";
import { check } from "k6";
import { randomItem } from "https://jslib.k6.io/k6-utils/1.2.0/index.js";
import { randomIntBetween } from "https://jslib.k6.io/k6-utils/1.2.0/index.js";

export let options = {
  vus: 10000,
  duration: "2m",
};

export default function () {
  // Generate random request type
  const request_type = randomItem([1, 2, 3]);

  // Generate random entity based on request type
  let entity;
  if (request_type === 1) {
    entity = {
      type: "content",
      id: String(randomIntBetween(1, 364583)),
    };
  } else if (request_type === 2) {
    entity = {
      type: "user",
      id: String(randomIntBetween(1, 52083)),
    };
  } else {
    entity = {
      type: "interaction",
      id: String(randomIntBetween(1, 104167)),
    };
  }

  // Generate random subject
  let subject = {
    type: "user",
    id: String(randomIntBetween(1, 52083)),
  };

  // Construct request payload
  let payload = {
    tenant_id: "t1",
    metadata: {
      snap_token: "n4QAAAAAAAA=",
      schema_version: "cojo0rv08b6g1j6m49q0",
      depth: 100,
    },
    entity: entity,
    permission: "view",
    subject: subject,
  };

  // Make HTTP request
  let response = http.post(
    "http://permify:3476/v1/tenants/t1/permissions/check",
    JSON.stringify(payload),
  );

  // Check response
  check(response, {
    "status is 200": (r) => r.status === 200,
  });
}
