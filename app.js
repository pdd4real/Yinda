const loginModal = document.querySelector("#loginModal");
const loginBtn = document.querySelector("#loginBtn");
const heroLoginBtn = document.querySelector("#heroLoginBtn");
const loginForm = document.querySelector("#loginForm");
const authErr = document.querySelector("#authErr");
const dispatchBtn = document.querySelector("#dispatchBtn");
const dispatchState = document.querySelector("#dispatchState");
const modeLabel = document.querySelector("#modeLabel");
const incidentTitle = document.querySelector("#incidentTitle");
const incidentDesc = document.querySelector("#incidentDesc");
const riskTag = document.querySelector("#riskTag");
const planResident = document.querySelector("#planResident");
const planStatus = document.querySelector("#planStatus");
const planEvent = document.querySelector("#planEvent");
const videoProof = document.querySelector(".video-proof");

function openLogin() {
  loginModal.hidden = false;
}

if (loginBtn && loginModal) loginBtn.addEventListener("click", openLogin);
if (heroLoginBtn && loginModal) heroLoginBtn.addEventListener("click", openLogin);

if (loginModal) {
  loginModal.addEventListener("click", (event) => {
    if (event.target.matches("[data-close]")) {
      loginModal.hidden = true;
      authErr.hidden = true;
    }
  });
}

if (loginForm) {
  loginForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const user = document.querySelector("#authUser").value.trim();
    const pass = document.querySelector("#authPass").value.trim();
    if (user === "admin" && pass === "admin") {
      window.location.href = "demo.html";
      return;
    }
    authErr.hidden = false;
  });
}

document.querySelectorAll(".rail").forEach((button) => {
  button.addEventListener("click", () => {
    document.querySelectorAll(".rail").forEach((item) => item.classList.remove("active"));
    button.classList.add("active");
    const labels = {
      night: "夜间加强模式",
      normal: "日间守护模式",
      away: "家属外出模式"
    };
    modeLabel.textContent = labels[button.dataset.mode];
  });
});

document.querySelectorAll(".resident").forEach((button) => {
  button.addEventListener("click", () => {
    document.querySelectorAll(".resident").forEach((item) => item.classList.remove("active"));
    button.classList.add("active");
    const risk = button.dataset.risk;
    const name = button.dataset.name;
    const room = button.dataset.room;
    riskTag.textContent = risk === "危急" ? "CRITICAL" : risk === "中" ? "MEDIUM" : "LOW";
    incidentTitle.textContent = `${name} · ${room}居家事件`;
    incidentDesc.textContent =
      risk === "危急"
        ? "声音事件“呼救”持续 4.8s，视频检测到疑似跌倒，建议 2 分钟内联动社区值班员与 120。"
        : risk === "中"
          ? "检测到非日常声音，需要家属确认并观察后续 15 分钟事件变化。"
          : "当前为低风险日常事件，系统自动归档并保留短窗口证据。";
    if (planResident) planResident.textContent = `${name} · ${room}`;
    if (planStatus) {
      planStatus.textContent = risk === "危急" ? "危急事件复核中" : risk === "中" ? "中风险观察中" : "低风险自动归档";
    }
    if (planEvent) planEvent.textContent = risk === "危急" ? "呼救" : risk === "中" ? "撞击声" : "环境噪声";
    if (videoProof) {
      videoProof.querySelector("strong").textContent =
        risk === "危急" ? "疑似跌倒 0.72" : risk === "中" ? "未见跌倒 0.18" : "无异常动作 0.04";
    }
    dispatchState.textContent = "等待总控确认";
  });
});

if (dispatchBtn) {
  dispatchBtn.addEventListener("click", () => {
    if (dispatchState) dispatchState.textContent = "已下发：社区网格员 2 分钟内确认";
    dispatchBtn.textContent = "任务已下发";
  });
}
