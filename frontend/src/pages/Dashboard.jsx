export default function Dashboard() {
  return (
    <div>
      <h1>Dashboard</h1>

      <button
        onClick={() => {
          window.location.href = "/upload";
        }}
      >
        Upload Resume
      </button>
    </div>
  );
}