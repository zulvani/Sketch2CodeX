import './App.css'

export default function App() {
  return (
    <div className="min-h-screen bg-gray-100 p-0">
      <div className="mx-auto max-w-md rounded bg-white p-6 shadow">

        {/* Row 1 */}
        <div class="v-row" className="mb-4 grid grid-cols-12 items-center gap-2">
          <div class="v-col" className="col-span-4 col-start-1">
            <div className="flex gap-2">
{/* Object Mapping image-card */}<div obj="image-card">
                  <div className="rounded w-full overflow-hidden shadow-sm">
                <div className="h-40 bg-gray-100 bg-center bg-cover flex items-center justify-center">Image</div>
                <div className="p-2 font-medium flex items-center justify-center">Title</div>
              </div>

</div>
            </div>
          </div>
          <div class="v-col" className="col-span-3 col-start-7">
            <div className="flex gap-2">
{/* Object Mapping label */}<div obj="label">
                  <label className="text-sm font-medium">
                Label
              </label>

</div>
            </div>
            <div className="flex gap-2">
{/* Object Mapping label */}<div obj="label">
                  <label className="text-sm font-medium">
                Label
              </label>

</div>
            </div>
            <div className="flex gap-2">
{/* Object Mapping label */}<div obj="label">
                  <label className="text-sm font-medium">
                Label
              </label>

</div>
            </div>
          </div>
        </div>

      </div>
    </div>
  )
}
